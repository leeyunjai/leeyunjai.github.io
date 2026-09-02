---
title: "두 시간에 LLM 하나, 명령 한 줄에 다이어그램 하나"
date: 2026-09-03T06:30:10+09:00
slug: "dev-github-minimind-archify"
summary: "이번 주 GitHub 주간 트렌딩에서 고른 개발자용 오픈소스 두 개. 64M 파라미터 언어모델을 GPU 한 장으로 직접 학습시키는 MiniMind, 시스템 설명을 아키텍처 다이어그램으로 바꿔 주는 에이전트 스킬 Archify를 라이선스·설치 명령과 함께 정리했습니다."
tags: ["GitHub", "Global"]
categories: ["Dev Picks"]
cover:
  image: "/images/posts/dev-github-minimind-archify.ko.png"
  alt: "이번 주 개발자 픽: MiniMind 57.7k 스타, Archify 이번 주 +25.5k 스타, 64M 파라미터, 학습 약 2시간"
  relative: false
draft: false
---

목요일 개발자 픽입니다. GitHub 주간 트렌딩(9월 첫째 주)에서 개발자가 바로 써 볼 수 있는 저장소 두 개를 골랐습니다. 하나는 언어모델을 "돌리는" 게 아니라 "만드는" 쪽이고, 하나는 설계 문서를 그림으로 바꾸는 도구입니다. 둘 다 README에 적힌 명령만 옮겼고, 확인되지 않은 항목은 그대로 표시했습니다.

## MiniMind

- 저장소: [github.com/jingyaogong/minimind](https://github.com/jingyaogong/minimind)
- 라이선스: Apache-2.0 · 언어: Python · 스타: 약 57.7k (이번 주 +1.9k)
- 최신 모델 릴리스: minimind-3 / minimind-3-moe, 2026-04-01 (README 기준)

64M 파라미터짜리 언어모델을 **처음부터 끝까지 직접 학습**시키는 프레임워크입니다. 사전학습, SFT, DPO·PPO·GRPO 같은 강화학습, 도구 호출, 지식 증류까지 한 저장소에 들어 있고 의존성이 적습니다. 모델을 내려받아 쓰는 게 아니라 토크나이저부터 학습 루프까지 코드를 읽으면서 만드는 구조라, LLM 내부가 어떻게 돌아가는지 몸으로 익히는 데 이만한 교재가 없습니다.

README가 말하는 최소 사양은 RTX 3090(24GB) 한 장, SFT 1에폭에 약 2시간, 클라우드 기준 비용 약 3위안입니다. 온디바이스 관점에서 64M은 Raspberry Pi 5나 Jetson에서도 추론이 되는 크기라, 학습은 데스크톱에서 하고 결과물을 보드에 올리는 흐름이 자연스럽게 나옵니다.

```bash
git clone --depth 1 https://github.com/jingyaogong/minimind
cd minimind && pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
# 학습된 모델로 바로 추론해 보기
modelscope download --model gongjy/minimind-3 --local_dir ./minimind-3
python eval_llm.py --load_from ./minimind-3
```

pip 미러 옵션(`-i ...aliyun...`)은 중국 내 속도용이라 국내에서는 빼도 됩니다. 모델 배포가 ModelScope 기준이라 `modelscope` 패키지가 필요합니다.

- 추천: LLM 구조를 코드로 이해하고 싶은 개발자, 소형 모델을 직접 만들어 임베디드에 올려 보려는 분. 성능 좋은 모델이 필요한 분에게는 아닙니다.

## Archify

- 저장소: [github.com/tt-a1i/archify](https://github.com/tt-a1i/archify)
- 라이선스: MIT · 언어: JavaScript/TypeScript (Node.js) · 스타: 약 43.7k (**이번 주 +25.5k**, 주간 트렌딩 1위권)
- 릴리스: 릴리스 페이지 최신 태그 v2.16.0, README는 2.17.0-dev.1 표기. 릴리스 페이지의 날짜 연도 표기가 2024로 나와 확인 필요

시스템을 말로 설명하면 **아키텍처·워크플로·시퀀스·데이터 흐름 다이어그램을 HTML 한 파일로** 만들어 주는 에이전트 스킬입니다. 입력은 타입이 정해진 JSON 명세이고, 검증을 거쳐 결정적으로 같은 결과가 나옵니다. 그래서 설계 문서를 git에 넣고 diff를 보거나, 두 버전을 비교(`compare`)하는 게 됩니다. Cursor, Claude Code, Codex CLI, OpenCode 같은 코딩 에이전트에 붙여서 쓰는 구조입니다.

이번 주에만 2만 5천 스타가 붙은 이유는 "에이전트에게 그림을 그리게 하는" 수요가 그만큼 크다는 뜻이겠습니다. 다만 성장 속도에 비해 릴리스 정보가 정리돼 있지 않아서, 위에 적은 대로 버전·날짜는 확인이 필요합니다.

```bash
npx skills add tt-a1i/archify -g
node archify/bin/archify.mjs doctor
node archify/bin/archify.mjs guide "Show CI/CD checks, approval, deploy, and rollback"
node archify/bin/archify.mjs preview workflow examples/agent-tool-call.workflow.json /tmp/workflow.html
```

- 추천: 설계 문서를 코드처럼 관리하고 싶은 팀, 코딩 에이전트를 이미 쓰고 있어서 문서화까지 맡기고 싶은 개발자. 마우스로 그리는 도구를 원하는 분에게는 맞지 않습니다.

## 오늘의 정리

| 프로젝트 | 라이선스 | 언어 | 스타 | 이번 주 | 한 줄 |
|---|---|---|---|---|---|
| MiniMind | Apache-2.0 | Python | 57.7k | +1.9k | 64M LLM을 GPU 한 장으로 직접 학습 |
| Archify | MIT | JS/TS | 43.7k | +25.5k | 설명 → 검증 가능한 다이어그램 HTML |

출처: [GitHub Trending (weekly)](https://github.com/trending?since=weekly), 각 저장소 README와 릴리스 페이지. 스타 수는 2026.09.03 조사 시점 기준입니다.
