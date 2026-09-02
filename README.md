# TechDrop

Hugo + PaperMod 기반 한/영 다국어 기술 블로그. https://leeyunjai.github.io/

## 구조

- `hugo.toml` — 사이트 설정. `ko`(기본, `/`) + `en`(`/en/`). AdSense/GA ID는 `[params]`의 `adsense`, `googleAnalytics`
- `content/posts/YYYY-MM-DD-<slug>.ko.md` / `.en.md` — 글. 같은 slug면 번역 쌍으로 묶여 언어 전환 버튼이 붙음
- `content/{about,privacy,archives,search}.{ko,en}.md` — 고정 페이지
- `layouts/partials/extend_head.html` — AdSense/GA 스크립트 (ID가 비어있으면 삽입 안 됨)
- `static/ads.txt` — AdSense 승인 후 publisher ID 기입
- `.github/workflows/hugo.yml` — `main` push 시 GitHub Pages 배포 (Hugo extended 최신, submodule 포함)
- `.claude/skills/weekly-post/SKILL.md` — `/weekly-post new`(월: 주간 신제품) / `/weekly-post deep`(목: 노트북→스마트폰→SBC→GitHub 인기 오픈소스→Hugging Face 인기 모델 순환 심층 리뷰)

## 로컬 실행

```bash
git clone --recurse-submodules https://github.com/leeyunjai/leeyunjai.github.io.git
cd leeyunjai.github.io
hugo server -D
```
