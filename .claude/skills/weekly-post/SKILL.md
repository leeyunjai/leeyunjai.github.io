---
name: weekly-post
description: DigitalBrain 블로그 글 자동 작성. 평일 하루 한 편. 인자 hw1(월)·hw2(화)는 노트북·스마트폰·가전·웨어러블 공통 풀에서 고르고, embedded(수 SBC·개발 보드·로봇), dev(목 GitHub 인기 오픈소스/Hugging Face 인기 모델 격주), brief(금 이번 주 브리핑). 조사 1회로 같은 slug의 .ko.md와 .en.md 두 파일을 content/posts/ 에 쓰고 main에 커밋·푸시한다.
---

# weekly-post

DigitalBrain(https://leeyunjai.github.io/)에 글 1편(한국어·영어 파일 각 1개)을 작성해 main에 커밋·푸시한다.
평일 하루 한 편이다.

## 0. 모드

인자로 모드를 받는다. 인자가 없으면 `TZ=Asia/Seoul date +%u` 로 요일을 보고 아래 표에서 고른다.

| 인자 | 요일 | 다루는 것 | categories |
|---|---|---|---|
| `hw1` | 월(1) | **하드웨어 공통 풀**에서 1개를 깊게 | `["Deep Dive"]` |
| `hw2` | 화(2) | **하드웨어 공통 풀**에서 1개를 깊게. 월요일과 다른 제품군 | `["Deep Dive"]` |
| `embedded` | 수(3) | SBC·개발 보드·로봇 1~2개를 깊게 | `["Deep Dive"]` |
| `dev` | 목(4) | GitHub 인기 오픈소스 **또는** Hugging Face 인기 모델 2~3개 | `["Dev Picks"]` |
| `brief` | 금(5) | 이번 주 브리핑. 국내 / 해외 / 소프트웨어 | `["Weekly Brief"]` |

### 하드웨어 공통 풀 (`hw1` / `hw2`)

매주 노트북이 나오지는 않는다. 그래서 월·화는 카테고리를 고정하지 않고 아래 네 제품군을 한 풀로 두고,
**그 주에 소재가 가장 좋은 것부터 고른다.**

| 제품군 | tag | 공급 |
|---|---|---|
| 노트북·PC | `Laptop` | 월 1~2회. CES·Computex·IFA에 몰린다 |
| 스마트폰·모바일 | `Smartphone` | 거의 매주 |
| 가전 | `Home Appliance` | 주 1~2회. 국내 출시가 꾸준하다 |
| 웨어러블 | `Wearable` | 워치·이어버드. 공백을 메우기 좋다 |

- `hw2`(화)는 **`hw1`(월)과 다른 제품군**에서 고른다. 이틀 연속 스마트폰은 안 된다.
- **가전은 기술적으로 쓸 것이 있는 쪽으로 한정한다.** 로봇청소기, TV·모니터, AI 기능이 붙은 가전.
  냉장고·세탁기처럼 스펙 나열밖에 안 나오는 제품은 다루지 않는다.
- **수요일과의 경계**: 로봇청소기 같은 소비자 완제품은 월·화(가전)로, 개발 보드와 산업·연구용 로봇은
  수요일(`embedded`)로 보낸다. 같은 제품을 양쪽에서 다루지 않는다.

토(6)·일(7)은 발행하지 않는다. 인자 없이 주말에 실행되면 아무것도 하지 않고
"주말은 발행일이 아닙니다"라고 답하고 끝낸다.

**`dev`는 GitHub와 Hugging Face를 격주로 번갈아 간다.** `ls content/posts` 에서 `dev-` 로 시작하는
가장 최근 글의 tags를 보고 반대쪽을 고른다. 이전 dev 글이 없으면 GitHub부터.

## 1. 준비 (필수)

1. `git fetch origin main && git checkout main && git pull origin main`
2. 오늘 날짜와 시각을 `TZ=Asia/Seoul date +%FT%T+09:00` 로 확인한다. front matter `date`는 이 값을 쓴다.
   **미래 시각 금지.** `buildFuture = false` 라서 빌드 시점보다 미래인 글은 사이트에서 빠진다.
3. **최근 30일 글의 front matter만 확인한다. 본문은 읽지 않는다.**

   ```bash
   for f in $(ls -t content/posts/*.ko.md | head -20); do echo "== $f"; sed -n '2,8p' "$f"; done
   ```

   여기 나온 **title에 등장하는 제품·프로젝트 이름은 이번 글의 주제로 삼지 않는다.** 파일명만 보면
   `brief-weekly-gadgets` 같은 slug에서 제품명을 놓치므로 title을 반드시 본다.

## 2. 조사 (1회, 웹 검색 최대 6회)

WebSearch로 조사한다. 한국어·영어 검색을 섞는다. 조사는 한 번만 하고 그 결과로 두 언어 파일을 모두 쓴다.
WebFetch는 원문 확인이 꼭 필요할 때만 쓰고, 차단되면 검색 결과로 대신한다.

### 소재가 없으면 쓰지 않는다 (가장 중요한 규칙)

매일 발행이지만 **매일 새 제품이 나오지는 않는다.** 해당 카테고리에서 최근 14일 내 발표된 실제 제품·릴리스가
없거나, 있어도 최근 30일 글에서 이미 다뤘다면 **글을 쓰지 않는다.** 커밋도 하지 않는다.
대신 실행 결과에 이렇게 한 줄 남기고 끝낸다.

> 오늘 <카테고리>에서 새로 다룰 소재가 없어 발행하지 않았습니다.

억지로 채운 글 한 편이 빈 하루보다 훨씬 나쁘다. 발행 빈도를 채우려고 오래된 제품을 다시 쓰거나,
루머·유출 기사를 제품인 것처럼 쓰거나, 스펙을 지어내면 안 된다.
카테고리 중에서는 **수요일 `embedded`가 가장 자주 빈다.** 격주로 빠지는 것이 정상이다.
월·화는 제품군이 네 개라 거의 매주 소재가 있어야 정상이다. 비면 검색 범위를 다시 확인한다.

### 2-1. `hw1` / `hw2` / `embedded` (월·화·수)

해당 풀에서 최근 14일 내 발표된 제품 1~2개를 골라 경쟁 제품과 비교하며 깊게 다룬다.
국내 출시 여부와 국내 가격을 별도 항목으로 표기한다. 미정이면 "확인 필요".

`hw1`·`hw2`는 위 **하드웨어 공통 풀** 표의 네 제품군을 모두 후보로 놓고 검색한다.
한 제품군만 검색해 보고 없다고 판단하지 말 것. 네 곳을 다 훑고도 없을 때만 발행하지 않는다.

`embedded`는 SBC·개발 보드·로봇을 모두 포함한다. **임베디드 관점을 반드시 넣는다.**
전원(전압·전류·전력 범위), 발열, 메모리 한계, 커넥터, 실제로 로봇이나 장비에 올릴 때 걸리는 지점.
데이터시트로 확인 안 된 전기적 수치는 절대 추측하지 말고 "확인 필요"라고 쓴다.

### 2-2. `dev` (목)

**GitHub 차례**: https://github.com/trending (weekly) 또는 "GitHub trending this week" 검색.
최근 30일 내 공개됐거나 큰 릴리스가 있었거나 스타가 급증한 저장소 2~3개.
각 항목: 저장소 링크, 라이선스, 주 언어, 스타 수(조사 시점), 최신 릴리스와 날짜, 무엇을 해결하는지 3~4문장,
실제 설치·실행 명령 또는 최소 예제(README에서 확인한 것만, 의사코드 금지), 추천 대상 1~2줄.

**Hugging Face 차례**: https://huggingface.co/models?sort=trending 또는
"Hugging Face trending models this week". 최근 30일 내 공개·갱신된 모델 2~3개.
온디바이스로 돌릴 수 있는 크기(대략 8B 이하 또는 양자화 버전 존재)와 비전·음성·로보틱스(VLA) 모델을 우선한다.
각 항목: 모델 카드 링크, 제작 조직, 라이선스, 파라미터 수, 태스크, 공개일,
특징과 벤치마크(모델 카드에 있는 것만), 실행 예제(모델 카드의 transformers / llama.cpp / OpenVINO 코드),
온디바이스(Raspberry Pi 5, Jetson, 노트북 GPU) 실행 가능성 1~2줄. 모르면 "확인 필요".

임베디드·로보틱스·온디바이스 AI·컴퓨터 비전·개발 도구 분야를 우선한다.

### 2-3. `brief` (금)

최근 7일 내 발표된 IT 신제품 3~5개. 노트북, 스마트폰, SBC, 로봇, AI 기기를 섞는다.

- **국내(Korea)**: 한국 제조사 제품이거나 이번 주 한국에 정식 출시·출시 발표된 제품. 가격은 원화 출하가.
- **해외(Global)**: 그 외. 가격은 발표 통화(USD/EUR 등) 그대로. 원화 환산 금지.
- **소프트웨어(Software)**: Hugging Face 인기 모델 또는 GitHub 인기 오픈소스 1~2개.
- 어느 섹션이든 소재가 없으면 "이번 주 국내 출시 소식은 확인되지 않았습니다." 한 줄만 쓴다.

**금요일 브리핑은 그 주의 허브다.** 이번 주 월~목에 발행한 글이 있으면 마지막에 링크로 묶는다.

```
## 이번 주 DigitalBrain
- [글 제목](/2026/09/07/laptop-.../)
```

같은 주 심층 글에서 이미 깊게 다룬 제품은 브리핑에서 **스펙 나열 정도로만 짧게 쓰고 그 글로 링크한다.**
의견과 비교를 반복하지 않는다.

### 공통 규칙

- **추측·창작 금지.** 검색 결과로 확인된 사실만 쓴다. 루머·유출·"출시 예정" 기사는 제품으로 세지 않는다.
- 스펙·가격·출시일이 확인되지 않으면 그 항목에 "확인 필요"(영문 "TBC")라고 쓴다. 채워 넣지 않는다.
- 출처 간 수치가 다르면 둘 다 적고 "확인 필요"를 붙인다.
- **각 제품·프로젝트마다 출처 링크 필수.** 제조사 공식 발표, 프로젝트 공식 저장소, 신뢰할 수 있는 매체
  (Notebookcheck, GSMArena, CNX Software, The Robot Report, 9to5Google, 국내 주요 경제·IT 매체 등) 우선.
- 부품명·칩 이름·라이브러리·저장소 이름은 영문 원문 그대로. (예: Snapdragon 8 Elite Gen 5, RP2350, llama.cpp)

## 3. 파일 (두 벌)

같은 slug의 파일 두 개를 쓴다. Hugo가 번역 쌍으로 묶어 언어 전환 버튼을 붙인다.

```
content/posts/YYYY-MM-DD-<slug>.ko.md
content/posts/YYYY-MM-DD-<slug>.en.md
```

- slug는 영문 kebab-case. **두 파일의 date·slug는 동일**해야 한다.
- slug는 **제품군 접두어**로 시작한다. 요일이 아니라 실제로 다룬 것을 따른다.
  `laptop-` `phone-` `appliance-` `wearable-` (월·화) / `embedded-` (수) / `dev-` (목) / `brief-` (금)
  예: `laptop-lg-gram-book-14`, `appliance-lg-roboking`, `wearable-galaxy-watch`,
  `embedded-jetson-orin-nano-2`, `dev-github-trending`, `brief-weekly-gadgets`
- 같은 날짜에 같은 slug가 있으면 뒤에 `-2`를 붙인다.

front matter (두 파일 공통 구조):

```yaml
---
title: "제목 (해당 언어)"
date: YYYY-MM-DDTHH:MM:SS+09:00   # 현재 시각(KST). 미래 금지. 두 파일 동일
slug: "<slug>"                    # 두 파일 동일
summary: "한 줄 요약 (해당 언어)"
tags: ["Laptop", "Smartphone", "Home Appliance", "Wearable", "SBC", "Robot", "AI Device", "GitHub", "Hugging Face", "Korea", "Global"]
categories: ["Deep Dive"]         # 0번 표 참고. 두 파일 동일
draft: false
---
```

`url:` 은 쓰지 않는다(언어별 경로가 충돌한다). 경로는 permalinks + slug 로 정해진다.
tags·categories는 영문으로 통일한다. tags는 실제 다룬 것만 넣는다.

## 4. 제목

제목은 밋밋한 설명문이 아니라 **리듬이 있는 한 줄**이어야 한다.

**만드는 법**

- **대구를 쓴다.** 앞뒤 구절의 음절 수와 조사를 맞춘다.
  `오늘 사는 노트북, 내년 오는 Jetson` (오늘/내년, 사는/오는)
- **같은 말을 되받는다.** 반복 자체가 리듬이 된다.
  `두 배는 두 배가 아니다`
- **대조를 세운다.** 기대와 실제, 값과 성능, 지금과 나중.
- 25자 안팎으로 끊는다. 콜론 뒤에 제품명을 나열하는 식은 쓰지 않는다.
- **제품·프로젝트 이름을 하나 이상 넣는다.** 검색 유입이 여기서 나온다. 가능하면 앞쪽에 둔다.
- 영어 제목도 같은 원칙으로 따로 만든다. 한국어 제목의 번역이 아니다.

**절대 넘지 않는 선**

리듬을 만들려고 **사실을 비틀지 않는다.** 본문에서 근거를 대지 못하는 표현은 제목에도 쓰지 않는다.
"두 배는 두 배가 아니다"는 본문이 40W와 25W 비교라는 근거를 대기 때문에 쓸 수 있다.
"충격", "실화냐", "역대급", "완벽", "최고" 같은 낚시 표현과, 제품을 써 보지 않고 써 본 것처럼 말하는
표현("직접 만져보니")은 쓰지 않는다.

**예시**

| 나쁨 | 좋음 |
|---|---|
| SBC 심층 리뷰: Jetson Orin Nano 2는 무엇이 달라졌나 | Jetson Orin Nano 2, 두 배는 두 배가 아니다 |
| 이번 주 신제품: LG 그램북 AI, 갤럭시 북6, Poco F9 | 오늘 사는 노트북, 내년 오는 Jetson |
| 노트북 심층 리뷰: A와 B 비교 | 같은 날 같은 값, 다른 선택 |
| GitHub 트렌딩 저장소 3선 | 작게 만들고, 빠르게 돌린다 |

`summary`는 반대로 **설명문으로 쓴다.** 제목이 압축하는 만큼 요약이 내용을 풀어 줘야 검색 결과에서
무슨 글인지 전달된다.

## 5. 본문

- **영어는 번역이 아니다.** 같은 조사 결과로 영어권 독자 기준으로 다시 쓴다.
- 분량: **한국어 1500~2500자**(공백 포함, front matter·표 제외), **영어 700~1200단어**(표 제외).
  한국어는 존댓말.

### `hw1` / `hw2` / `embedded` 구조

도입 2~3문장 → `## {제품명}` 상세(스펙 표) → 경쟁 제품 비교 표 → 장단점과 어떤 사용자에게 맞는지 →
국내 출시 여부 → `## 총평` / `## Verdict`

### `dev` 구조

도입 → `## {저장소 또는 모델 이름}` × 2~3 (링크·라이선스·크기 → 해결하는 문제 → 설치·실행 코드 블록 →
추천 대상) → `## 오늘의 정리` / `## Wrap-up`

### `brief` 구조

한국어: 도입 2~3문장 → `## 국내` → `## 해외` → `## 소프트웨어` → `## 이번 주 요약` 표 → `## 이번 주 DigitalBrain` 링크
영어: `## Korea` → `## Global` → `## Software` → `## This Week at a Glance` → `## This Week on DigitalBrain`

제품마다: 맥락 1~2문장 → 핵심 스펙 bullet 3~6개 → 가격/출시일 → 의견 1~2줄 → 출처 링크

## 6. 이미지 (글마다 최소 1장, 최대 2장)

**외부 사진은 쓰지 않는다.** 이 실행 환경은 외부 이미지 호스트 다운로드가 전부 차단돼 있고, 제조사 사진은 저작권 문제가 있다.
대신 **글에서 확인된 수치로 카드를 직접 그린다.** `scripts/postimg.py`가 렌더링한다. 한글 폰트는 저장소에 들어 있다.

### 6-1. 커버 카드 (필수, 언어별 1장씩)

```bash
pip install -q pillow     # 세션마다 한 번
cat > /tmp/cover.ko.json <<'EOF'
{"kicker": "심층 리뷰 · SBC · 로봇",
 "title": "<한국어 글 제목 그대로>",
 "date": "YYYY.MM.DD",
 "stats": [{"value": "78 TOPS", "label": "AI 연산"}, {"value": "8GB", "label": "메모리"}]}
EOF
python3 scripts/postimg.py cover /tmp/cover.ko.json static/images/posts/<slug>.ko.png
# 영어도 같은 방식으로 /tmp/cover.en.json → static/images/posts/<slug>.en.png
```

- `stats`는 **본문에 출처와 함께 적힌 수치만** 3~4개. 본문에 없는 숫자는 카드에도 없다.
- `kicker`는 카테고리 · 태그를 해당 언어로. `title`은 글 제목과 글자 하나까지 같게.
- 만든 JSON은 `scripts/img-specs/<slug>.<lang>.json` 으로 저장해 둔다. 나중에 다시 그릴 때 쓴다.

### 6-2. 비교 차트 (심층 리뷰에 두 제품 수치 비교 표가 있을 때, 선택)

```bash
cat > /tmp/cmp.ko.json <<'EOF'
{"title": "A vs B", "a": "A (신형)", "b": "B (현행)",
 "rows": [{"label": "AI 연산 (TOPS)", "a": 78, "b": 67}, {"label": "최소 전력 (W)", "a": 15, "b": 7}],
 "note": "출처: ..."}
EOF
python3 scripts/postimg.py compare /tmp/cmp.ko.json static/images/posts/<slug>-compare.ko.png
```

`rows`의 숫자는 본문 비교 표에 있는 값만 쓴다. 단위는 `label`에 적는다.

### 6-3. 글에 연결

front matter에 커버를 넣는다 (두 파일 각각 자기 언어 이미지):

```yaml
cover:
  image: "/images/posts/<slug>.ko.png"
  alt: "<카드에 적힌 수치를 문장으로>"
  relative: false
```

비교 차트는 본문의 비교 표 **바로 아래**에 넣는다. 캡션에 무엇을 보라는지 한 줄 쓴다.

```markdown
![A와 B 수치 비교: 항목1, 항목2](/images/posts/<slug>-compare.ko.png "표를 막대로 그린 것입니다. 최소 전력 차이를 보세요.")
```

### 6-4. 확인과 커밋

- 생성한 PNG를 **Read 도구로 열어 본다.** 글자가 타일을 넘치거나 깨지면 라벨을 줄여서 다시 그린다.
- `git add` 에 `static/images/posts/<slug>*.png` 와 `scripts/img-specs/<slug>*.json` 을 포함한다.

### 절대 규칙

- **AI로 제품 사진을 만들지 않는다.** 실물처럼 보이는 가짜 이미지 한 장이 "확인된 것만"이라는 이 사이트의 약속을 깨뜨린다.
- 외부 이미지 URL을 핫링크하지 않는다. 언젠가 끊기고, 저작권도 남의 것이다.
- 카드의 숫자는 전부 본문에 출처와 함께 있어야 한다. 카드가 본문보다 앞서가면 안 된다.

## 7. 검증

- 두 파일의 front matter YAML이 유효한지, `date`·`slug`·`tags`·`categories`가 같은지, `draft: false` 인지.
- 모든 링크가 http(s) 또는 `/` 로 시작하는지.
- 분량:
  ```bash
  sed '1,/^---$/d' content/posts/<file>.en.md | grep -v '^|' | wc -w
  sed '1,/^---$/d' content/posts/<file>.ko.md | grep -v '^|' | LC_ALL=C.UTF-8 wc -m
  ```
- `hugo` 가 설치돼 있으면 `hugo --gc --minify` 로 빌드해 본다. 없으면 건너뛴다.

## 8. 커밋·푸시 (main)

```bash
git add content/posts/YYYY-MM-DD-<slug>.ko.md content/posts/YYYY-MM-DD-<slug>.en.md \
        static/images/posts/<slug>*.png scripts/img-specs/<slug>*.json
git commit -m "post: <English title>"
git push -u origin main
```

푸시 후 GitHub Actions(`Deploy Hugo site to GitHub Pages`)가 실행된다. 실패하면 로그를 보고 고친다.

## 9. AdSense 신청 시점 알림 (매 실행 마지막)

```bash
POSTS=$(ls content/posts/*.ko.md 2>/dev/null | wc -l)
ADSENSE=$(grep -E '^[[:space:]]*adsense[[:space:]]*=' hugo.toml | sed 's/.*"\(.*\)".*/\1/')
echo "posts=$POSTS adsense='$ADSENSE'"
```

- `POSTS`가 **25 이상**이고 `ADSENSE`가 **빈 문자열**이면, 실행 결과 메시지 마지막에 아래를 포함한다.

  > **AdSense 신청 시점입니다.** 글이 N편 쌓였습니다. https://adsense.google.com 에서 사이트를 등록하세요.
  > 계정을 만들면 바로 나오는 publisher ID(`ca-pub-...`)를 알려주시면 `hugo.toml`의 `params.adsense`와
  > `static/ads.txt`에 넣어 배포하겠습니다. 그 코드가 사이트에 올라가야 심사가 시작됩니다.

- 이미 적용됐거나 25편 미만이면 아무것도 하지 않는다.

**AdSense ID는 직접 만들거나 추측하지 않는다.** 사용자가 알려준 값만 넣는다.
