# ARC Current

사용후 배터리 시장 정보 블로그. Hugo + PaperMod, 한국어/영어 다국어.

- Production URL: https://current.arc.ai.kr/
- Korean: /ko/  English: /en/

## Structure

- content/ko/posts/ : Korean posts
- content/en/posts/ : English posts
- hugo.yaml : site configuration
- .github/workflows/deploy.yml : auto build and deploy on push to main
- static/CNAME : custom domain

## Writing a post

Create a markdown file in both content/ko/posts/ and content/en/posts/ with the same filename (this links them for the language switcher).

Front matter example:

    ---
    title: "제목"
    date: 2026-08-01T09:00:00+09:00
    categories: ["market"]   # market | tech | policy
    tags: ["태그"]
    draft: false
    ---

Push to main and GitHub Actions deploys automatically.

## Local preview

    hugo server -D

Requires Hugo extended v0.164.0 or later.
