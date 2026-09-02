---
name: weekly-post
description: DigitalBrain 블로그 주간 글 자동 작성. 인자 new(월요일)는 최근 7일 IT 신제품을 국내/해외/소프트웨어(Hugging Face 인기 모델·GitHub 인기 오픈소스)로 나눠 정리, 인자 deep(목요일)은 노트북→스마트폰→SBC→GitHub 인기 오픈소스→Hugging Face 인기 모델 순환 심층 리뷰. 조사 1회로 같은 slug의 .ko.md와 .en.md 두 파일을 content/posts/ 에 쓰고 main에 커밋·푸시한다.
---

# weekly-post

DigitalBrain(https://leeyunjai.github.io/) 블로그에 글 1편(한국어·영어 파일 각 1개)을 작성해 main에 커밋·푸시한다.
일주일에 2편. 요일(또는 인자)에 따라 글 성격이 다르다.

## 0. 모드 결정

인자가 있으면 인자를 따른다. 없으면 `TZ=Asia/Seoul date +%u` 로 요일을 판별한다.

| 인자 | 요일 | 모드 | 글 성격 |
|---|---|---|---|
| `new` | 월(1)·화(2)·수(3) | **신제품 모드** | 이번 주 IT 신제품 3~5개(국내/해외) + 소프트웨어 1~2개 |
| `deep` | 목(4)·금(5)·토(6)·일(7) | **심층 리뷰 모드** | 한 카테고리를 골라 깊게 |

심층 리뷰 카테고리는 다음 순서로 순환한다.

**노트북 → 스마트폰 → SBC → GitHub 인기 오픈소스 → Hugging Face 인기 모델 → 노트북 …**

`ls content/posts` 에서 파일명에 `deep-dive-` 가 들어간 가장 최근 파일의 카테고리 접두어
(`laptop` / `smartphone` / `sbc` / `github` / `huggingface`)를 보고 그 다음 카테고리를 고른다. 없으면 노트북부터 시작한다.

## 1. 작성 전 준비 (필수)

1. `git fetch origin main && git checkout main && git pull origin main` 으로 최신 상태를 맞춘다.
2. 오늘 날짜와 현재 시각을 `TZ=Asia/Seoul date +%FT%T+09:00` 로 확인한다. front matter `date`는 이 값(현재 시각)을 쓴다.
   **미래 시각 금지.** `buildFuture = false` 라서 빌드 시점보다 미래인 글은 사이트에서 빠진다.
3. **최근 30일 글의 front matter만 확인한다. 본문은 읽지 않는다.**

   ```bash
   for f in $(ls -t content/posts/*.ko.md | head -12); do echo "== $f"; sed -n '2,8p' "$f"; done
   ```

   여기서 나온 **title에 등장하는 제품·프로젝트 이름은 이번 글의 주제로 삼지 않는다.** 파일명만 보면
   `weekly-new-gadgets` 같은 slug에서 제품명을 놓치므로 title을 반드시 본다.

   - 신제품 모드: 이미 다룬 제품은 후보에서 뺀다.
   - 심층 리뷰 모드: **순환 차례인 카테고리라도, 다루려던 제품이 최근 30일 title에 이미 있으면
     그 카테고리를 건너뛰고 순환의 다음 카테고리로 넘어간다.** 같은 제품을 각도만 바꿔 다시 쓰지 않는다.
     예: 주간 글에서 노트북 A와 B를 다뤘다면, 그 주 심층 리뷰는 A와 B가 아니라 스마트폰이나 SBC로 간다.
   - 같은 날짜에 이미 글이 있으면 그 글과 주제가 겹치지 않는지 특히 주의한다.
   - 신제품 모드와 심층 리뷰가 같은 제품을 스치더라도, 심층 리뷰는 **비교 대상·수치·결론이 모두 새로워야**
     한다. 스펙 표와 의견이 주간 글과 비슷해지면 주제를 바꾼다.

## 2. 조사 (1회, 웹 검색 최대 6회)

WebSearch로 조사한다. **검색은 최대 6회.** 한국어·영어 검색을 섞는다. 조사는 한 번만 하고, 그 결과로 두 언어 파일을 모두 쓴다.
WebFetch는 원문 확인이 꼭 필요할 때만 쓰고, 차단되면 검색 결과로 대신한다.

### 2-1. 신제품 모드

대상은 **최근 7일 내 발표된** IT 신제품: 노트북, 스마트폰, SBC(단일 보드 컴퓨터), 로봇, AI 기기.
실제 제품 **3~5개**. 카테고리를 섞는다.

**국내 / 해외를 분리한다.**

- **국내(Korea)**: 한국 제조사 제품이거나 이번 주 한국에 정식 출시·출시 발표된 제품. 가격은 원화(출하가).
- **해외(Global)**: 그 외. 가격은 발표 통화(USD/EUR 등) 그대로. 원화 환산 금지.
- 국내 소식이 없으면 국내 섹션에 "이번 주 국내 출시 소식은 확인되지 않았습니다." / "No Korean launches were confirmed this week." 한 줄만 쓴다. 억지로 채우지 않는다.

**소프트웨어(Software) 섹션을 하나 더 둔다.** 이번 주 Hugging Face 인기 모델 또는 GitHub 인기 오픈소스 중 **1~2개**.
- 고르는 법: https://huggingface.co/models?sort=trending , https://github.com/trending (weekly). 최근 30일 내 공개·큰 릴리스·스타 급증한 것만.
- 임베디드/로보틱스/온디바이스 AI/컴퓨터 비전/개발 도구를 우선한다.
- 각 항목: 링크(모델 카드 또는 저장소), 제작 조직, 라이선스, 크기(파라미터 수 또는 스타 수), 무엇을 하는지 2~3문장, 설치·실행 한 줄(README/모델 카드에서 확인한 것만), 의견 1~2줄.
- 하드웨어 제품(3~5개)과는 별도로 센다. 검색 6회 중 1~2회를 여기에 쓴다.

### 2-2. 심층 리뷰 모드 (노트북 / 스마트폰 / SBC)

해당 카테고리에서 최근 7일 내 발표된 제품 **1~2개**를 골라 경쟁 제품과 비교하며 깊게 다룬다.
7일 내 발표가 없으면 최근 30일까지 넓히되, 파일명에 이미 나온 제품은 제외한다.
국내 출시 여부·국내 가격을 별도 항목으로 표기한다. (미정이면 "확인 필요" / "TBC")

### 2-3. 심층 리뷰 모드 (GitHub 인기 오픈소스)

이번 주 GitHub에서 인기 있는 개발자용 오픈소스 프로젝트 **2~3개**를 소개한다.
https://github.com/trending (weekly) 또는 "GitHub trending this week" 검색으로 고른다. 최근 30일 내 새로 공개됐거나 큰 릴리스가 있었거나 스타가 급증한 것만 고른다.
분야는 임베디드/로보틱스/온디바이스 AI/컴퓨터 비전/개발 도구를 우선한다. (예: ROS 2 패키지, MicroPython/ESP-IDF 라이브러리, OpenVINO/llama.cpp 계열, FastAPI 생태계, CLI 도구)

각 프로젝트마다 반드시 적는다:
- 저장소 링크, 라이선스, 주 언어, 스타 수(조사 시점), 최신 릴리스 버전과 날짜
- 무엇을 해결하는지 3~4문장
- 실제 설치·실행 명령 또는 최소 예제 코드 (README에서 확인한 것만. 의사코드 금지)
- 어떤 개발자에게 유용한지 1~2줄

### 2-4. 심층 리뷰 모드 (Hugging Face 인기 모델)

이번 주 Hugging Face에서 인기 있는 모델 **2~3개**를 소개한다.
https://huggingface.co/models?sort=trending 또는 "Hugging Face trending models this week" 검색으로 고른다. 최근 30일 내 공개·갱신된 모델만 고른다.
온디바이스로 돌릴 수 있는 크기(대략 8B 이하, 또는 양자화 버전이 있는 것)와 비전·음성·로보틱스(VLA) 모델을 우선한다.

각 모델마다 반드시 적는다:
- 모델 카드 링크, 제작 조직, 라이선스, 파라미터 수, 태스크(텍스트/비전/음성/VLA 등), 공개일
- 무엇을 잘하는지·벤치마크 수치(모델 카드에 있는 것만) 3~4문장
- 실행 예제: 모델 카드의 transformers / llama.cpp / OpenVINO 예제 코드 (모델 카드에서 확인한 것만. 의사코드 금지)
- 온디바이스(Raspberry Pi 5, Jetson, 일반 노트북 GPU) 실행 가능성 1~2줄. 모르면 "확인 필요"

### 공통 규칙

- **추측·창작 금지.** 검색 결과로 확인된 사실만 쓴다. 루머·유출·"출시 예정" 기사는 제품으로 세지 않는다.
- 스펙·가격·출시일이 확인되지 않으면 그 항목에 "확인 필요"(영문 "TBC")라고 쓴다. 채워 넣지 않는다.
- 출처 간 수치가 다르면 둘 다 적고 "확인 필요"를 붙인다.
- **각 제품·프로젝트마다 출처 링크 필수.** 제조사 공식 발표, 프로젝트 공식 저장소, 신뢰할 수 있는 매체(Notebookcheck, GSMArena, CNX Software, The Robot Report, 9to5Google, 국내 주요 경제·IT 매체 등)를 우선한다.
- 부품명·칩 이름·라이브러리·저장소 이름은 영문 원문 그대로. (예: Snapdragon 8 Elite Gen 5, RP2350, llama.cpp)

## 3. 파일 (두 벌)

조사 결과로 **같은 slug의 파일 두 개**를 쓴다. Hugo가 번역 쌍으로 묶어 언어 전환 버튼을 붙인다.

```
content/posts/YYYY-MM-DD-<slug>.ko.md
content/posts/YYYY-MM-DD-<slug>.en.md
```

- slug는 영문 kebab-case, **두 파일의 date·slug는 동일**해야 한다.
- 신제품 모드 slug 예: `weekly-new-gadgets`, 제품이 뚜렷하면 `weekly-gadgets-jetson-orin-nano-2-poco-f9`
- 심층 리뷰 slug는 반드시 `<category>-deep-dive-<subject>` 형식: `laptop-deep-dive-lg-gram-book-14`, `smartphone-deep-dive-...`, `sbc-deep-dive-...`, `github-deep-dive-...`, `huggingface-deep-dive-...`
- 같은 날짜에 같은 slug가 있으면 slug 뒤에 `-2` 를 붙인다.

front matter (YAML, 두 파일 공통 구조):

```yaml
---
title: "제목 (해당 언어)"
date: YYYY-MM-DDTHH:MM:SS+09:00   # 현재 시각(KST). 미래 금지. 두 파일 동일
slug: "<slug>"                    # 두 파일 동일
summary: "한 줄 요약 (해당 언어)"
tags: ["Laptop", "Smartphone", "SBC", "Robot", "AI Device", "GitHub", "Hugging Face", "Korea", "Global"]   # 실제 다룬 것만, 두 파일 동일
categories: ["Weekly New Gadgets"]   # 심층 리뷰 모드는 ["Deep Dive"]. 두 파일 동일
draft: false
---
```

`url:` 은 쓰지 않는다(언어별 경로가 충돌한다). 경로는 permalinks + slug 로 정해진다.
tags·categories는 영문으로 통일한다(두 언어의 태그 페이지가 같은 이름으로 묶이도록).

## 4. 본문

- **영어는 번역이 아니다.** 같은 조사 결과를 바탕으로 영어권 독자 기준으로 자연스럽게 다시 쓴다. (통화·단위·비교 대상은 영어권 독자에게 익숙한 것으로)
- 분량: **한국어 1500~2500자**(공백 포함, front matter·표 제외), **영어 700~1200단어**(표 제외). 한국어는 존댓말.

### 신제품 모드 구조 (.en.md)

```
{intro, 2-3 sentences}

## Korea
### {Product name}
{1-2 sentences of context}
- Key specs (3~6 bullets)
- Price / Release (region, date)
- Take: {1~2 lines of own opinion}
- Source: [Outlet](URL)

## Global
### {Product name}
...

## Software
### {Model or repo name}
{1-2 sentences of context}
- Org / License / Size (params or stars)
- Install or run: `one line from README or model card`
- Take: {1~2 lines}
- Source: [Hugging Face or GitHub](URL)

## This Week at a Glance
| Product | Category | Region | Key specs | Price | Release |
(소프트웨어 행은 Region을 "Software", Price를 라이선스로 적는다)
```

### 신제품 모드 구조 (.ko.md)

```
{도입 2~3문장}

## 국내
### {제품명}
{맥락 1~2문장}
- 핵심 스펙 (bullet 3~6개)
- 가격 / 출시일(지역)
- 의견: {직접 의견 1~2줄. 교육용 로봇·임베디드 관점 코멘트 환영}
- 출처: [매체명](URL)

## 해외
### {제품명}
...

## 소프트웨어
### {모델명 또는 저장소명}
{맥락 1~2문장}
- 제작 / 라이선스 / 크기(파라미터 수 또는 스타 수)
- 설치·실행: `README 또는 모델 카드의 한 줄`
- 의견: {1~2줄}
- 출처: [Hugging Face 또는 GitHub](URL)

## 이번 주 요약
| 제품 | 카테고리 | 지역 | 핵심 스펙 | 가격 | 출시일 |
(소프트웨어 행은 지역을 "소프트웨어", 가격을 라이선스로 적는다)
```

### 심층 리뷰 모드 구조

각 언어 파일: 도입 → `## {Product}` 상세(스펙 표, 경쟁 제품 비교, 장단점, 어떤 사용자에게 맞는지, 국내 출시 여부) → `## Verdict` / `## 총평`.
GitHub 차례에는 `## {Project name}` 아래 저장소/라이선스/스타/버전, 해결하는 문제, 설치·실행 예제(코드 블록), 추천 대상 순으로 쓴다.
Hugging Face 차례에는 `## {Model name}` 아래 모델 카드/조직/라이선스/파라미터/태스크, 특징과 벤치마크, 실행 예제(코드 블록), 온디바이스 실행 가능성 순으로 쓴다.

## 5. 검증

- 두 파일의 front matter YAML이 유효한지, `date`·`slug`·`tags`·`categories`가 같은지, `draft: false` 인지 확인한다.
- 모든 링크가 http(s)로 시작하는지 확인한다.
- 분량 확인:
  ```bash
  sed '1,/^---$/d' content/posts/<file>.en.md | grep -v '^|' | wc -w
  sed '1,/^---$/d' content/posts/<file>.ko.md | grep -v '^|' | LC_ALL=C.UTF-8 wc -m
  ```
- `hugo` 가 설치되어 있으면 `hugo --gc --minify` 로 빌드해 본다. 없으면 건너뛴다.

## 6. 커밋·푸시 (main)

```bash
git add content/posts/YYYY-MM-DD-<slug>.ko.md content/posts/YYYY-MM-DD-<slug>.en.md
git commit -m "post: <English title>"
git push -u origin main
```

푸시 후 GitHub Actions(`Deploy Hugo site to GitHub Pages`)가 실행된다. 실패하면 로그를 보고 고친다.

## 7. AdSense 신청 시점 알림 (매 실행 마지막)

푸시가 끝나면 아래를 실행해 AdSense 신청 시점이 됐는지 확인한다.

```bash
POSTS=$(ls content/posts/*.ko.md 2>/dev/null | wc -l)
ADSENSE=$(grep -E '^[[:space:]]*adsense[[:space:]]*=' hugo.toml | sed 's/.*"\(.*\)".*/\1/')
echo "posts=$POSTS adsense='$ADSENSE'"
```

- `POSTS`가 **25 이상**이고 `ADSENSE`가 **빈 문자열**이면, 실행 결과 메시지 마지막에 아래 내용을 반드시 포함한다.
  (Routine 푸시 알림으로 사용자에게 전달된다.)

  > **AdSense 신청 시점입니다.** 글이 N편 쌓였습니다. https://adsense.google.com 에서 사이트를 등록하고 심사를 신청하세요.
  > 승인 후 publisher ID(`ca-pub-...`)를 알려주시면 `hugo.toml`의 `params.adsense`와 `static/ads.txt`에 넣어 배포하겠습니다.
  > 심사 전 확인: 소개 페이지에 연락처(이메일), 개인정보처리방침 링크, 최근 글의 출처 링크.

- `ADSENSE`가 비어 있지 않으면(이미 적용됨) 아무것도 하지 않는다.
- `POSTS`가 25 미만이면 아무것도 하지 않는다. 매 실행마다 알리지 않는다.

**AdSense ID는 직접 만들거나 추측하지 않는다.** 사용자가 알려준 값만 넣는다.
