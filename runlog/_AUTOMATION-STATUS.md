# 자동 발행 현재 상태: 중지됨

## 무슨 일이 있었나

2026-09-02 밤 ~ 09-03 새벽, Routine(예약 실행) 5개를 만들어 평일 자동 발행을 시도했으나
**예약 세션이 GitHub에 푸시하지 못해** 글이 사이트에 올라가지 않았다.

### 확인한 사실

| 시도 | 내용 | 결과 |
|---|---|---|
| 실제 실행 (09-03 06:03) | dev 모드, 10분, 출력 44K 토큰, 비용 $2.43 | 커밋 0건. 글은 썼으나 어디에도 푸시 안 됨 |
| 진단 1 | 저장소 확인 + main 푸시 | 31초 만에 종료, 푸시 없음 |
| 진단 2 | 저장소 없으면 클론 후 main 푸시 | 110초, 푸시 없음 |
| 진단 3 | 지정 브랜치 / 새 브랜치 / main 세 곳 모두 시도 | **세 곳 모두 실패** |

세 브랜치 어디에도 푸시되지 않았고, PR도 만들어지지 않았다.
예약 세션의 로그는 다른 세션에서 열람할 수 없어 에러 원문은 확보하지 못했다.

**원인: 이 Routine들에 GitHub 커넥터가 붙어 있지 않다.**

Routine을 MCP 도구(`create_trigger`)로 만들면 아래 경고가 나온다. 만들 때 이를 놓쳤다.

> this trigger stores no MCP connectors, so the sessions it fires will run without
> connector (mcp__<server>__*) tools. ... If the routine needs connectors, create it
> from a session that holds them, or ask the user to create it from the claude.ai routines UI.

GitHub 연동 자체는 계정에 연결돼 있다(claude.ai → 사용자 지정 → 커넥터 → GitHub 연동 ✓).
문제는 **예약 세션이 그 연동을 물려받지 못한다**는 것이다. 그래서 컨테이너에 GitHub 자격증명이 없고,
`git push` 가 어느 브랜치로도 되지 않는다.

`create_trigger` 에 `connectors` 인자를 넣어 붙이는 것도 시도했으나 조직 정책으로 막혀 있다.

> create_trigger: the connectors parameter is not available for this organization.

대화형 세션(사람이 연 Claude Code 세션)은 커넥터를 물고 있어 정상적으로 푸시된다.

## 지금 상태

- Routine 5개는 **모두 비활성화**했다. 이름 앞에 `[중지]`가 붙어 있다.
  그대로 두면 매일 새벽 $2.4씩 쓰면서 결과물이 없다.
- 스킬(`.claude/skills/weekly-post/SKILL.md`)은 그대로 쓸 수 있다. 이미지 단계는 뺐다.

## 다시 켜려면 — claude.ai Routines UI에서 새로 만들 것

코드로 만든 Routine에는 커넥터를 붙일 수 없다. **웹 UI에서 직접 만들어야 한다.**

1. claude.ai → Claude Code → Routines (또는 사용자 지정 화면의 Routines)
2. 새 Routine 만들기. 저장소는 `leeyunjai/leeyunjai.github.io`, GitHub 커넥터가 붙는지 확인
3. 모델 Claude Sonnet 5, 알림 켜기
4. 아래 프롬프트를 그대로 붙여넣기 (요일별로 하나씩, 총 5개)
5. **먼저 하나만 만들어 수동 실행**해 보고, `runlog/` 에 파일이 올라오면 나머지를 만든다
6. 기존 `[중지]` Routine 5개는 지운다

### cron (UTC 기준, 한국시간 03:00)

| 요일 | cron | 인자 |
|---|---|---|
| 월 | `0 18 * * 0` | `hw1` |
| 화 | `0 18 * * 1` | `hw2` |
| 수 | `0 18 * * 2` | `embedded` |
| 목 | `0 18 * * 3` | `dev` |
| 금 | `0 18 * * 4` | `brief` |

### 붙여넣을 프롬프트 (`<MODE>` 를 위 표의 인자로 바꿀 것)

```
저장소 leeyunjai/leeyunjai.github.io 에서 다음을 수행하세요.

1. git fetch origin main && git checkout main && git pull origin main
2. .claude/skills/weekly-post/SKILL.md 를 읽고, 인자 `<MODE>` 모드로 그 지시를 그대로 따르세요.
3. 최근 14일 내 새로 다룰 소재가 없거나 최근 30일 글에서 이미 다룬 것뿐이면
   글을 쓰지 말고 그 사실만 한 줄로 보고하고 끝내세요. 억지로 채우지 마세요.
4. 글을 썼으면 다른 것을 하기 전에 먼저 main에 커밋·푸시하세요.
   이 저장소는 main 직접 푸시가 승인된 워크플로입니다. PR을 만들지 마세요.
5. 푸시가 실패하면 에러 메시지 원문 전체를 최종 보고 첫 줄에 쓰세요. 조용히 끝내지 마세요.
6. runlog/<날짜>-<MODE>.md 에 실행 기록을 남기고 함께 푸시하세요.
7. GitHub Actions "Deploy Hugo site to GitHub Pages" 결과를 확인하세요.
```

## 그때까지 발행하는 법

대화형 세션에서 직접 실행하면 정상 동작한다. 실제로 09-03 개발자 픽 글은 이 방식으로 발행했다.

```
/weekly-post hw1     (월: 하드웨어 ①)
/weekly-post hw2     (화: 하드웨어 ②)
/weekly-post embedded (수: SBC·로봇)
/weekly-post dev     (목: 개발자 픽)
/weekly-post brief   (금: 이번 주 브리핑)
```
