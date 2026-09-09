---
title: "매트 포콕 스킬, 코드 대신 명령 한 줄"
date: 2026-09-10T03:10:52+09:00
slug: "dev-mattpocock-skills-chrome-devtools"
summary: "이번 주 GitHub 트렌딩에서 스타 25만 개를 넘긴 매트 포콕의 에이전트 스킬 저장소와, 에이전트용 플러그인 시스템을 새로 얹은 Chrome DevTools MCP v1.9.0을 골랐습니다."
tags: ["GitHub"]
categories: ["Dev Picks"]
cover:
  image: "/images/posts/dev-mattpocock-skills-chrome-devtools.ko.png"
  alt: "커버 카드: 매트 포콕 스킬 저장소 25만 7천 스타(주간 +1만 3천), Chrome DevTools MCP 5만 1천 스타, v1.9.0 2026년 9월 8일 출시, 라이선스 MIT·Apache-2.0"
  relative: false
draft: false
---

이번 주 GitHub 트렌딩은 에이전트에게 무엇을 "설치"해 줄 것인가로 모였습니다. 하나는 코드 한 줄 없이
지침 파일만으로 25만 스타를 모은 스킬 저장소, 다른 하나는 브라우저 제어 도구에 확장 기능을 얹은
MCP 서버의 새 릴리스입니다. 둘 다 `npx` 한 줄로 설치가 끝난다는 점이 공통점입니다.

## mattpocock/skills

TypeScript 강사로 유명한 매트 포콕(Matt Pocock)이 공개한 이 저장소는 코드가 아니라 **에이전트 스킬**,
즉 AI 코딩 에이전트가 읽고 따르는 지침·스크립트 모음입니다. 조사 시점 기준 **257,729 스타**이며
이번 주에만 **13,419 스타**가 늘었습니다. 라이선스는 **MIT**, README에 명시된 주 배포 형태는 셸 스크립트
기반 설치기입니다. 최신 릴리스 태그는 저장소 페이지에서 확인되지 않아 "확인 필요"로 남깁니다.

설명에 따르면 이 저장소의 스킬들은 실제 엔지니어링 경험을 바탕으로, 개발자와 AI 에이전트가 같은 용어를
쓰게 하고, 피드백 루프로 코드 품질을 높이고, 아키텍처 일관성을 지키도록 돕는 작은 조합형 도구라고
설명합니다. 특정 모델에 종속되지 않고 어떤 AI 모델과도 함께 쓸 수 있다는 점을 강조합니다.

설치는 README에 적힌 대로 한 줄입니다.

```bash
# Claude Code 플러그인으로
claude plugins install mattpocock-skills
# 또는 세션 안에서
/plugin install mattpocock-skills

# 다른 에이전트/도구에서
npx skills@latest add mattpocock/skills

# 설치 후
/setup-matt-pocock-skills
```

**추천 대상**: Claude Code나 Codex 같은 에이전트를 매일 쓰면서, 코드 리뷰·네이밍·아키텍처 규칙을
매번 프롬프트로 반복 설명하는 데 지친 시니어 개발자.

눈에 띄는 것은 개별 스킬 내용보다 패키징 방식입니다. 스킬은 지침을 적은 마크다운 파일에 스크립트가
딸려 오는 폴더일 뿐이고, 시스템 프롬프트에 전부 밀어 넣는 대신 에이전트가 필요할 때 골라 읽게 합니다.

- 출처: [github.com/mattpocock/skills](https://github.com/mattpocock/skills)

## ChromeDevTools/chrome-devtools-mcp

Chrome DevTools 팀이 만든 MCP(Model Context Protocol) 서버로, AI 코딩 에이전트가 실제 크롬 브라우저를
열어 성능 추적, 네트워크·콘솔 디버깅, Puppeteer 기반 브라우저 자동화를 수행하게 해 줍니다. 언어는
**TypeScript**, 라이선스는 **Apache-2.0**. 조사 시점 스타는 **51,455개**(이번 주 +1,014)입니다.

**최신 릴리스는 v1.9.0, 2026년 9월 8일 출시**로 조사 시점 바로 전날입니다. 릴리스 노트에는
"Agent Plugins 1.0 패키지 추가"와 "JavaScript 실행 도구를 끄는 옵션 추가"가 올라와 있습니다.
매트 포콕의 스킬이 지침을 설치하는 쪽이라면, 이 릴리스는 도구 쪽에 확장 슬롯을 만든 셈입니다.

설치는 MCP 클라이언트 설정 파일에 아래를 추가합니다.

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

헤드리스로 가볍게 쓰려면 slim 모드도 있습니다.

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--slim", "--headless"]
    }
  }
}
```

**추천 대상**: 에이전트에게 실제 웹앱을 열어 성능·네트워크 문제를 스스로 디버깅하게 만들고 싶은
프런트엔드·QA 개발자.

위 두 설정 블록이 설치의 전부입니다. 별도 빌드 단계 없이 `npx -y chrome-devtools-mcp@latest` 가
매번 최신 배포 버전을 받아 오기 때문입니다. `--slim --headless` 옵션은 CI나 화면 없는 서버에서
쓸모없는 디버깅 명령까지 에이전트에게 내주지 않도록 도구 목록을 줄여 줍니다.

- 출처: [github.com/ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp), [릴리스 페이지](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases)

## 오늘의 정리

두 저장소 모두 "설치 명령 한 줄"을 README 맨 위에 내세웁니다. 스킬은 지침을, MCP 서버는 도구를
패키지 매니저처럼 설치하는 방식이 같은 주에 나란히 트렌딩에 올랐다는 것이 눈에 띕니다. 이 흐름이
한 곳만의 일도 아닙니다. OpenAI도 Codex용 `openai/skills` 카탈로그를 운영했지만 지금은 이 저장소가
새 OpenAI Plugins 저장소로 안내하도록 바뀌었습니다. 지침이든 도구든 에이전트의 동작을 설치 가능한
단위로 패키징해 한 줄 명령으로 꽂아 넣는 방향으로, 여러 진영이 같은 모양에 수렴하고 있습니다.

| 항목 | 스타(조사 시점) | 이번 주 증가 | 라이선스 |
|---|---|---|---|
| mattpocock/skills | 257,729 | +13,419 | MIT |
| ChromeDevTools/chrome-devtools-mcp | 51,455 | +1,014 | Apache-2.0 |
