#!/usr/bin/env python3
"""ARC Current 포스트 커버 썸네일(1200x630 PNG) 생성기.

사용 예:
    python3 scripts/make_thumbnail.py --md content/ko/posts/why-arc-current.md
    python3 scripts/make_thumbnail.py --title "제목" --axis recycling --category market --slug my-post
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = Path(__file__).resolve().parent / "fonts" / "pretendard"
DEFAULT_OUT_DIR = REPO_ROOT / "static" / "images" / "covers"

CANVAS_W, CANVAS_H = 1200, 630
PAD_X = 72
TOP_BAR_H = 10

BG_COLOR = (11, 15, 25)          # 짙은 네이비 (다크 고정 배경)
TEXT_PRIMARY = (248, 250, 252)
TEXT_MUTED = (148, 163, 184)

# 축(axis)별 액센트 컬러. 다크 배경 위에서 대비가 확보되는 톤으로 선정.
AXIS_COLORS = {
    "recycling": (45, 212, 191),
    "second-life": (52, 211, 153),
    "policy": (129, 140, 248),
    "players": (56, 189, 248),
    "safety": (251, 191, 36),
    "supply": (251, 146, 60),
    "default": (100, 116, 139),
}
AXIS_LABELS = {
    "recycling": "RECYCLING",
    "second-life": "SECOND-LIFE",
    "policy": "POLICY",
    "players": "PLAYERS",
    "safety": "SAFETY",
    "supply": "SUPPLY",
    "default": "ARC CURRENT",
}
CATEGORY_LABELS = {
    "market": "시장동향",
    "tech": "기술",
    "policy": "정책·규제",
}

FONT_REGULAR = FONT_DIR / "Pretendard-Regular.otf"
FONT_BOLD = FONT_DIR / "Pretendard-Bold.otf"
FONT_EXTRABOLD = FONT_DIR / "Pretendard-ExtraBold.otf"


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list:
    """공백 기준 어절 단위로 줄바꿈. 한 어절이 max_width보다 길면 글자 단위로 쪼갠다."""
    words = text.split(" ")
    lines = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textlength(candidate, font=fnt) <= max_width:
            current = candidate
            continue
        if current:
            lines.append(current)
        if draw.textlength(word, font=fnt) <= max_width:
            current = word
            continue
        chunk = ""
        for ch in word:
            if draw.textlength(chunk + ch, font=fnt) <= max_width:
                chunk += ch
            else:
                if chunk:
                    lines.append(chunk)
                chunk = ch
        current = chunk
    if current:
        lines.append(current)
    return lines or [""]


def fit_title(
    draw: ImageDraw.ImageDraw,
    text: str,
    max_width: int,
    max_height: int,
    start_size: int = 72,
    min_size: int = 34,
    step: int = 4,
    max_lines: int = 4,
):
    """제목이 영역 안에 들어갈 때까지 폰트 크기를 줄이며 줄바꿈한다."""
    text = " ".join(text.split())  # 개행 등 모든 공백을 정규화 (Pillow는 멀티라인 폭 측정 불가)
    size = start_size
    while size >= min_size:
        fnt = font(FONT_EXTRABOLD, size)
        lines = wrap_text(draw, text, fnt, max_width)
        line_height = int(size * 1.3)
        if len(lines) <= max_lines and line_height * len(lines) <= max_height:
            return fnt, lines, line_height
        size -= step

    # 최소 크기로도 안 들어가면 줄 수를 제한하고 말줄임표 처리
    fnt = font(FONT_EXTRABOLD, min_size)
    lines = wrap_text(draw, text, fnt, max_width)
    line_height = int(min_size * 1.3)
    fit_lines = max(1, max_height // line_height)
    if len(lines) > fit_lines:
        lines = lines[:fit_lines]
        last = lines[-1]
        while draw.textlength(last + "…", font=fnt) > max_width and len(last) > 1:
            last = last[:-1]
        lines[-1] = last.rstrip() + "…"
    return fnt, lines, line_height


def draw_accent_glow(base: Image.Image, color: tuple) -> Image.Image:
    """우상단에 축 색상의 은은한 원형 글로우를 겹쳐 완전한 평면을 피한다."""
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    cx, cy, r = CANVAS_W - 120, -180, 420
    odraw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, 26))
    return Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")


def render(title: str, axis: str, category: str | None) -> Image.Image:
    axis_color = AXIS_COLORS.get(axis, AXIS_COLORS["default"])
    axis_label = AXIS_LABELS.get(axis, AXIS_LABELS["default"])

    base = Image.new("RGB", (CANVAS_W, CANVAS_H), BG_COLOR)
    base = draw_accent_glow(base, axis_color)
    draw = ImageDraw.Draw(base)

    # 상단 액센트 바
    draw.rectangle([0, 0, CANVAS_W, TOP_BAR_H], fill=axis_color)

    # 카테고리 배지 (좌상단)
    badge_font = font(FONT_BOLD, 24)
    badge_pad_x, badge_pad_y = 20, 10
    badge_top = 48
    text_w = draw.textlength(axis_label, font=badge_font)
    badge_h = 24 + badge_pad_y * 2
    badge_box = [PAD_X, badge_top, PAD_X + text_w + badge_pad_x * 2, badge_top + badge_h]
    draw.rounded_rectangle(badge_box, radius=badge_h / 2, fill=axis_color)
    draw.text(
        (PAD_X + badge_pad_x, badge_top + badge_pad_y - 1),
        axis_label,
        font=badge_font,
        fill=BG_COLOR,
    )

    # 우상단 카테고리 라벨 (있는 경우)
    if category:
        cat_label = CATEGORY_LABELS.get(category, category)
        meta_font = font(FONT_REGULAR, 22)
        mw = draw.textlength(cat_label, font=meta_font)
        draw.text((CANVAS_W - PAD_X - mw, badge_top + badge_pad_y - 2), cat_label, font=meta_font, fill=TEXT_MUTED)

    # 제목
    title_area_top = badge_top + badge_h + 40
    footer_divider_y = CANVAS_H - 92
    max_title_width = CANVAS_W - PAD_X * 2
    max_title_height = footer_divider_y - title_area_top - 10

    title_font, lines, line_height = fit_title(draw, title, max_title_width, max_title_height)
    total_h = line_height * len(lines)
    y = title_area_top + max(0, (max_title_height - total_h) // 2)
    for line in lines:
        draw.text((PAD_X, y), line, font=title_font, fill=TEXT_PRIMARY)
        y += line_height

    # 하단 구분선 + 워드마크
    draw.line([(PAD_X, footer_divider_y), (CANVAS_W - PAD_X, footer_divider_y)], fill=(30, 41, 59), width=1)

    dot_r = 5
    dot_cy = footer_divider_y + 36
    draw.ellipse([PAD_X, dot_cy - dot_r, PAD_X + dot_r * 2, dot_cy + dot_r], fill=axis_color)

    brand_font = font(FONT_BOLD, 24)
    draw.text((PAD_X + dot_r * 2 + 12, dot_cy - 15), "ARC Current", font=brand_font, fill=TEXT_PRIMARY)

    url_font = font(FONT_REGULAR, 20)
    url_label = "current.arc.ai.kr"
    uw = draw.textlength(url_label, font=url_font)
    draw.text((CANVAS_W - PAD_X - uw, dot_cy - 13), url_label, font=url_font, fill=TEXT_MUTED)

    return base


def read_front_matter(md_path: Path):
    """front matter 구분자는 '---'만 있는 독립된 줄에서만 인식한다.
    (front matter 값 안에 '---' 문자열이 포함돼도 오인하지 않도록)"""
    lines = md_path.read_text(encoding="utf-8").splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise ValueError(f"{md_path}: front matter(---...---)를 찾을 수 없습니다.")

    # 들여쓰기 없이 '---'만 있는 줄만 구분자로 인정한다
    # (YAML block scalar 안에 들여쓰기된 '---' 내용 줄과 혼동하지 않도록)
    end_idx = next((i for i in range(1, len(lines)) if lines[i].rstrip("\r\n") == "---"), None)
    if end_idx is None:
        raise ValueError(f"{md_path}: front matter를 닫는 '---'를 찾을 수 없습니다.")

    front_matter = yaml.safe_load("".join(lines[1:end_idx])) or {}
    body = "".join(lines[end_idx + 1 :])
    return front_matter, body


def write_front_matter(md_path: Path, front_matter: dict, body: str) -> None:
    fm_text = yaml.safe_dump(front_matter, allow_unicode=True, sort_keys=False, default_flow_style=False, width=1000)
    md_path.write_text(f"---\n{fm_text}---\n{body}", encoding="utf-8")


def resolve_axis(explicit_axis: str | None, tags: list) -> str:
    if explicit_axis:
        return explicit_axis
    for tag in tags:
        if tag in AXIS_COLORS:
            return tag
    return "default"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--md", type=Path, help="포스트 md 파일 경로 (title/categories/tags를 front matter에서 읽는다)")
    parser.add_argument("--title", help="제목 (--md 미지정 시 필수, --md와 함께 쓰면 override)")
    parser.add_argument("--category", choices=list(CATEGORY_LABELS), help="market | tech | policy")
    parser.add_argument("--axis", choices=list(AXIS_COLORS), help="축 태그 (미지정 시 tags에서 자동 탐지)")
    parser.add_argument("--slug", help="출력 파일명(확장자 제외). --md 미지정 시 필수")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    parser.add_argument(
        "--no-update-front-matter",
        action="store_true",
        help="--md 사용 시에도 front matter의 cover 항목을 자동으로 갱신하지 않는다",
    )
    args = parser.parse_args()

    front_matter, body = (None, None)
    if args.md:
        front_matter, body = read_front_matter(args.md)
        title = args.title or str(front_matter.get("title", "")).strip()
        categories = front_matter.get("categories") or []
        category = args.category or (categories[0] if categories else None)
        tags = front_matter.get("tags") or []
        axis = resolve_axis(args.axis, tags)
        slug = args.slug or args.md.stem
    else:
        if not args.title:
            parser.error("--md 또는 --title 중 하나는 반드시 필요합니다.")
        if not args.slug:
            parser.error("--md 없이 사용할 때는 --slug를 명시해야 합니다.")
        title = args.title
        category = args.category
        axis = args.axis or "default"
        slug = args.slug

    if not title:
        parser.error("제목을 확인할 수 없습니다 (front matter의 title이 비어 있음).")

    image = render(title, axis, category)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_path = args.out_dir / f"{slug}.png"
    image.save(out_path, format="PNG", optimize=True)

    size_kb = out_path.stat().st_size / 1024
    print(f"[make_thumbnail] axis={axis} category={category} slug={slug}")
    print(f"[make_thumbnail] saved {out_path} ({image.width}x{image.height}, {size_kb:.1f} KB)")

    if args.md and not args.no_update_front_matter:
        rel_path = f"/images/covers/{slug}.png"
        front_matter["cover"] = {"image": rel_path, "alt": title, "relative": False}
        write_front_matter(args.md, front_matter, body)
        print(f"[make_thumbnail] {args.md} front matter cover -> {rel_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
