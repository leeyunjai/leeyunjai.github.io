# DigitalBrain

Hugo + PaperMod 한/영 기술 블로그. https://leeyunjai.github.io/

- 글: `content/posts/YYYY-MM-DD-<slug>.ko.md` / `.en.md`
- 배포: `main` push 시 GitHub Actions → GitHub Pages
- 자동 작성: 평일 매일 1편. `hw1`(월) `hw2`(화) `embedded`(수) `dev`(목) `brief`(금)

```bash
git clone --recurse-submodules https://github.com/leeyunjai/leeyunjai.github.io.git
hugo server -D
```

## 글 이미지

- `scripts/postimg.py` — 글의 검증된 수치로 커버 카드(1200×630, OG 겸용)와 비교 차트를 그립니다. 외부 사진은 쓰지 않습니다.
- `scripts/fonts/NotoSansKR-{400,700}.ttf` — 카드 렌더링용. SIL Open Font License 1.1.
- `scripts/img-specs/` — 각 이미지의 입력 JSON. 다시 그릴 때 씁니다.

## 아이콘 라이선스

- 본문·목록·메뉴 아이콘: [Lucide](https://lucide.dev) 기하를 따른 인라인 SVG. ISC License, 출처 표기 의무 없음.
- 헤더 로고 마크: 자체 제작.
- 외부 요청 없이 `layouts/_partials/icon.html`에서 인라인으로 그립니다. 아이콘을 추가하려면 이 파일에 이름 하나를 더하면 됩니다.
- 출처 표기가 필요한 세트(Font Awesome Free는 CC BY 4.0, Flaticon은 표기 필수)는 쓰지 않았습니다.
