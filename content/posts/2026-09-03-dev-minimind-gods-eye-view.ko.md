---
title: "미니마인드는 작게, 갓츠아이뷰는 크게"
date: 2026-09-03T07:57:31+09:00
slug: "dev-minimind-gods-eye-view"
summary: "이번 주 GitHub 트렌딩에서 64M 파라미터 언어모델을 2시간 만에 학습하는 MiniMind와, 브라우저에서 실시간 위성·항공·해상 데이터를 3D 지구본으로 보여주는 God's Eye View를 골랐다."
tags: ["GitHub"]
categories: ["Dev Picks"]
draft: false
---

이번 주 GitHub 트렌딩은 방향이 정반대인 두 프로젝트가 나란히 올라왔습니다. 하나는 언어모델을 최대한 작게, 다른 하나는 지구 전체의 실시간 데이터를 최대한 크게 끌어모읍니다. 온디바이스 AI와 개발 도구 쪽에서 각각 이번 주 급증한 저장소 두 개를 골라봤습니다.

## MiniMind

- 저장소: [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
- 라이선스: Apache License 2.0
- 언어: Python
- 스타: 57,757 (조사 시점), 이번 주 +1,949
- 최신 릴리스: minimind-3 / minimind-3-moe (2026-04-01)

MiniMind는 64M 파라미터짜리 언어모델을 라이브러리에 감싸이지 않은 순수 코드로 처음부터 학습시키는 프로젝트입니다. README는 학습 비용을 "3위안(약 0.43달러), 2시간"으로 소개합니다. RTX 3090(24GB) 한 장으로 돌아가며, 학습·추론 코드가 모두 짧고 그대로 읽을 수 있게 짜여 있어 트랜스포머 학습 파이프라인 내부를 직접 뜯어보고 싶은 사람에게 맞습니다.

```bash
git clone --depth 1 https://github.com/jingyaogong/minimind
cd minimind && pip install -r requirements.txt

# 추론
python eval_llm.py --load_from ./minimind-3

# 학습
cd trainer && python train_pretrain.py
cd trainer && python train_full_sft.py
```

C-Eval 24.89%, CMMLU 25.38%, 영어권 벤치마크(ARC/PIQA/OpenBookQA/HellaSwag/SocialIQA)는 과제별로 23~50%대를 기록했습니다(README 기준). LoRA로 정렬한 minimind-3-exam 변형은 여기서 약 2.9%p 더 오릅니다. 64M 규모라 상용 서비스에 바로 쓸 성능은 아니지만, "LLM이 어떻게 학습되는가"를 코드 한 줄씩 따라가며 배우려는 개발자나 학생에게 추천할 만합니다.

## God's Eye View

- 저장소: [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view)
- 라이선스: MIT
- 언어: JavaScript
- 스타: 16,070, 이번 주 +12,042 (이번 주 트렌딩 중 증가 폭이 가장 큼)
- 최신 릴리스: 확인 필요 (저장소에 별도 릴리스 태그 없이 커밋 단위로 갱신 중)

God's Eye View는 브라우저에서 돌아가는 실시간 공간정보 시각화 도구입니다. OpenSky Network·adsb.lol의 항공기, AISStream의 선박, CelesTrak의 위성, USGS의 지진, NASA FIRMS의 산불, Launch Library 2의 발사 일정, 도시별 CCTV, 지오로케이션된 라디오 방송국까지 공개 API를 모아 하나의 3D 지구본 위에 겹쳐 보여줍니다. 지도 렌더링은 Cesium ion·Google Maps·Esri·OpenStreetMap을 함께 씁니다.

```bash
npm install
npm run doctor
npm run dev
# http://localhost:4173 에서 확인
```

Pinokio를 쓴다면 Discover 탭에 저장소 주소를 붙여 넣는 방식으로도 설치할 수 있다고 안내되어 있습니다. 전문 GIS 툴 없이 브라우저만으로 실시간 항공·해상·우주 트래킹 대시보드를 만들어보고 싶은 프론트엔드 개발자, 공개 데이터로 시각화 사이드 프로젝트를 찾는 사람에게 특히 볼 만합니다.

국내 출시나 가격과는 무관한 순수 오픈소스 프로젝트라 별도 국내 출시 여부는 해당하지 않습니다.

## 오늘의 정리

두 프로젝트는 방향이 반대지만 배우는 지점은 비슷합니다. MiniMind는 모델을 작게 만들어 학습 과정 자체를 들여다보게 하고, God's Eye View는 여러 공개 API를 하나의 화면에 모아 데이터를 다루는 법을 보여줍니다. 둘 다 코드를 그대로 실행해볼 수 있는 저장소이니, 관심 있는 쪽부터 클론해서 열어보시길 권합니다.
