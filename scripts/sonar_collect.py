#!/usr/bin/env python3
"""Sonar 수집기: 네이버 뉴스 / 해외 RSS / arXiv에서 후보 기사를 모아
sonar/candidates/YYYY-MM-DD.json 에 저장한다.
"""

import json
import logging
import re
import sys
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlparse

import feedparser
import requests
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SONAR_DIR = REPO_ROOT / "sonar"
CONFIG_PATH = SONAR_DIR / "config.yaml"
SEEN_PATH = SONAR_DIR / "seen.json"
CANDIDATES_DIR = SONAR_DIR / "candidates"
ENV_PATH = REPO_ROOT / ".env"

NAVER_NEWS_URL = "https://openapi.naver.com/v1/search/news.json"
ARXIV_API_URL = "https://export.arxiv.org/api/query"
HTTP_TIMEOUT = 15

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("sonar_collect")


def load_env(path: Path) -> dict:
    env = {}
    if not path.exists():
        return env
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_seen(path: Path) -> set:
    if not path.exists():
        return set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return set(data.get("links", []))
    except (json.JSONDecodeError, OSError) as e:
        log.warning("seen.json 로드 실패, 빈 목록으로 시작: %s", e)
        return set()


def save_seen(path: Path, seen: set) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"links": sorted(seen)}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def strip_html(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", "", text)
    return text.replace("&quot;", '"').replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").strip()


def collect_naver_news(env: dict, config: dict) -> list:
    client_id = env.get("NAVER_CLIENT_ID")
    client_secret = env.get("NAVER_CLIENT_SECRET")
    if not client_id or not client_secret:
        log.error("NAVER_CLIENT_ID/SECRET이 .env에 없어 네이버 뉴스 수집을 건너뜁니다.")
        return []

    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }
    naver_cfg = config.get("naver_news", {})
    display = naver_cfg.get("display", 20)
    sort = naver_cfg.get("sort", "date")
    axes = naver_cfg.get("axes", {})

    items = []
    for axis, keywords in axes.items():
        for keyword in keywords:
            try:
                resp = requests.get(
                    NAVER_NEWS_URL,
                    headers=headers,
                    params={"query": f'"{keyword}"', "display": display, "sort": sort},
                    timeout=HTTP_TIMEOUT,
                )
                resp.raise_for_status()
                data = resp.json()
            except (requests.RequestException, ValueError) as e:
                log.warning("네이버 뉴스 수집 실패 (axis=%s, keyword=%s): %s", axis, keyword, e)
                continue

            for it in data.get("items", []):
                link = it.get("originallink") or it.get("link")
                if not link:
                    continue
                pub_date = it.get("pubDate", "")
                try:
                    pub_date_iso = parsedate_to_datetime(pub_date).isoformat()
                except (TypeError, ValueError):
                    pub_date_iso = pub_date

                source = urlparse(link).netloc

                items.append(
                    {
                        "axis": axis,
                        "title": strip_html(it.get("title", "")),
                        "link": link,
                        "source": source,
                        "published": pub_date_iso,
                        "snippet": strip_html(it.get("description", "")),
                        "origin": "naver_news",
                        "matched_keyword": keyword,
                    }
                )
            log.info("네이버 뉴스: axis=%s keyword=%s -> %d건", axis, keyword, len(data.get("items", [])))
    return items


def collect_rss(config: dict) -> list:
    rss_cfg = config.get("rss_feeds", {})
    sources = rss_cfg.get("sources", [])
    keyword_filter = [kw.lower() for kw in rss_cfg.get("keyword_filter", [])]

    items = []
    for source in sources:
        name = source.get("name", "unknown")
        url = source.get("url")
        try:
            resp = requests.get(url, timeout=HTTP_TIMEOUT, headers={"User-Agent": "Mozilla/5.0 (compatible; SonarBot/1.0)"})
            resp.raise_for_status()
            feed = feedparser.parse(resp.content)
            if feed.bozo and not feed.entries:
                raise ValueError(feed.bozo_exception)
        except Exception as e:
            log.warning("RSS 수집 실패 (%s, %s): %s", name, url, e)
            continue

        matched = 0
        for entry in feed.entries:
            title = entry.get("title", "")
            summary = strip_html(entry.get("summary", ""))
            haystack = f"{title} {summary}".lower()
            if keyword_filter and not any(kw in haystack for kw in keyword_filter):
                continue

            link = entry.get("link")
            if not link:
                continue

            published = entry.get("published", "") or entry.get("updated", "")
            try:
                published_iso = parsedate_to_datetime(published).isoformat()
            except (TypeError, ValueError):
                published_iso = published

            items.append(
                {
                    "axis": "recycling/second-life",
                    "title": strip_html(title),
                    "link": link,
                    "source": name,
                    "published": published_iso,
                    "snippet": summary[:300],
                    "origin": "rss",
                    "matched_keyword": None,
                }
            )
            matched += 1
        log.info("RSS: %s -> %d건 (필터 통과)", name, matched)
    return items


def collect_arxiv(config: dict) -> list:
    arxiv_cfg = config.get("arxiv", {})
    lookback_days = arxiv_cfg.get("lookback_days", 30)
    max_results = arxiv_cfg.get("max_results_per_query", 20)
    queries = arxiv_cfg.get("queries", [])

    cutoff = datetime.now(timezone.utc) - timedelta(days=lookback_days)

    items = []
    for query in queries:
        search_query = f'abs:"{query}" OR ti:"{query}"'
        try:
            resp = requests.get(
                ARXIV_API_URL,
                params={
                    "search_query": search_query,
                    "sortBy": "submittedDate",
                    "sortOrder": "descending",
                    "max_results": max_results,
                },
                timeout=HTTP_TIMEOUT,
            )
            resp.raise_for_status()
            feed = feedparser.parse(resp.content)
        except Exception as e:
            log.warning("arXiv 수집 실패 (query=%s): %s", query, e)
            continue

        matched = 0
        for entry in feed.entries:
            published = entry.get("published", "")
            try:
                published_dt = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            except ValueError:
                published_dt = None

            if published_dt and published_dt < cutoff:
                continue

            link = entry.get("link") or entry.get("id")
            if not link:
                continue

            journal = entry.get("arxiv_journal_ref", "arXiv")

            items.append(
                {
                    "axis": "tech-research",
                    "title": strip_html(entry.get("title", "")).replace("\n", " ").strip(),
                    "link": link,
                    "source": journal,
                    "published": published_dt.isoformat() if published_dt else published,
                    "snippet": strip_html(entry.get("summary", ""))[:300],
                    "origin": "arxiv",
                    "matched_keyword": query,
                }
            )
            matched += 1
        log.info("arXiv: query=%s -> %d건 (%d일 이내)", query, matched, lookback_days)
    return items


def dedupe(items: list, seen: set) -> tuple:
    """링크 기준 중복 제거. 이번 배치 내 중복과 이전 수집분(seen) 모두 제외한다."""
    fresh = []
    batch_links = set()
    for item in items:
        link = item["link"]
        if link in batch_links or link in seen:
            continue
        batch_links.add(link)
        fresh.append(item)
    return fresh, batch_links


def main() -> int:
    env = load_env(ENV_PATH)
    config = load_config(CONFIG_PATH)
    seen = load_seen(SEEN_PATH)

    all_items = []
    all_items.extend(collect_naver_news(env, config))
    all_items.extend(collect_rss(config))
    all_items.extend(collect_arxiv(config))

    fresh_items, new_links = dedupe(all_items, seen)

    today = datetime.now().strftime("%Y-%m-%d")
    out_path = CANDIDATES_DIR / f"{today}.json"
    CANDIDATES_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(fresh_items, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    seen.update(new_links)
    save_seen(SEEN_PATH, seen)

    by_axis = {}
    for item in fresh_items:
        by_axis[item["axis"]] = by_axis.get(item["axis"], 0) + 1

    log.info("수집 완료: 총 %d건 (수집 시도 %d건 중 중복 제외)", len(fresh_items), len(all_items))
    for axis, count in sorted(by_axis.items()):
        log.info("  - %s: %d건", axis, count)
    log.info("저장 위치: %s", out_path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
