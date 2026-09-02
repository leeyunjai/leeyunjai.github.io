# 자동 발행 현재 상태: 작동 중

예약 실행 **하나**가 매일 새벽 03:00(KST)에 돌고, **스킬이 요일을 보고 그날 카테고리를 정한다.**

| 요일 | 모드 | 다루는 것 |
|---|---|---|
| 월 | `hw1` | 노트북·스마트폰·가전·웨어러블 중 하나 |
| 화 | `hw2` | 같은 풀에서, 월요일과 다른 제품군 |
| 수 | `embedded` | SBC·개발 보드·로봇 |
| 목 | `dev` | GitHub 인기 오픈소스 / Hugging Face 인기 모델 (격주) |
| 금 | `brief` | 이번 주 브리핑 + 그 주 글 링크 |
| 토·일 | — | 즉시 종료. 아무것도 하지 않는다 |

Routine 프롬프트에는 `hw1`이 적혀 있지만 **스킬이 그 인자를 무시하고 요일로 결정한다.**
요일별로 Routine을 5개 만들 필요가 없다.

## 왜 이렇게 됐나

Routine을 MCP 도구(`create_trigger`)로 만들면 커넥터가 붙지 않아 **예약 세션이 GitHub에 푸시하지 못한다.**
2026-09-02 밤에 만든 5개가 전부 그랬다. 진단 3회(지정 브랜치·새 브랜치·main) 모두 실패했고,
`connectors` 인자로 붙이는 것도 조직 정책으로 막혀 있다.

> create_trigger: the connectors parameter is not available for this organization.

**claude.ai Routines UI에서 만든 것만 작동한다.** 지금 살아 있는 Routine이 그것이다.
UI로 만든 Routine은 에이전트가 수정할 수 없어서(`update_trigger` 거부), cron을 매일로 두고
스킬 쪽에서 요일 분기를 하도록 맞췄다.

## 손댈 때 주의

- **Routine을 늘리지 말 것.** 하나로 5일을 담당한다.
- Routine 프롬프트의 `hw1`은 바꾸지 않아도 된다. 스킬이 무시한다.
- 카테고리나 요일 배치를 바꾸려면 `.claude/skills/weekly-post/SKILL.md` 의 0번 표만 고치면 된다.
- 새 Routine이 필요하면 **반드시 claude.ai Routines UI에서** 만들 것. MCP로 만든 것은 푸시가 안 된다.

## 수동 발행

대화형 세션에서는 인자가 우선한다.

```
/weekly-post hw1   hw2   embedded   dev   brief
```
