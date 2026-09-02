---
title: "오늘 사는 노트북, 내년 오는 Jetson"
date: 2026-09-02T15:00:00+09:00
slug: "brief-weekly-gadgets"
summary: "같은 날 출시된 국내 실속형 14형 노트북 2종, NVIDIA 차세대 보급형 Jetson, 가격이 오른 Poco F9 시리즈를 정리했습니다."
tags: ["Laptop", "SBC", "Smartphone", "GitHub", "Korea", "Global"]
categories: ["Weekly Brief"]
cover:
  image: "/images/posts/brief-weekly-gadgets.ko.png"
  alt: "이번 주 브리핑: 그램북 AI 14, 뉴 갤럭시 북6, Jetson Orin Nano 2, Poco F9 Pro 핵심 수치"
  relative: false
draft: false
---
9월 첫째 주는 애플 9월 9일 행사와 IFA 베를린을 앞둔 조용한 주였지만, 눈에 띄는 제품이 네 가지 있었습니다. 국내에서는 LG전자와 삼성전자가 같은 날 실속형 14형 노트북을 출시했습니다. 해외에서는 NVIDIA가 로봇용 보급형 Jetson을 새로 내놓았고, Poco는 가격이 꽤 오른 F9 시리즈를 발표했습니다.

## 국내

### LG 그램북 AI 2026 14형 (14U40V)

- CPU: Intel Core Series 3 (Wildcat Lake)
- 배터리: 61.2Wh, 최대 30.5시간 (LG 자체 기준)
- 무게/두께: 1.29kg / 14.9mm, 알루미늄 외장
- 디스플레이: 14형. 해상도·패널 종류는 확인 필요
- 메모리/저장장치: 확인 필요 (구성에 따라 다름)
- 가격: 출하가 145만 원부터
- 출시: 9월 1일 발표, 9월 7일부터 LGE닷컴과 주요 온라인몰에서 판매, 9월 중순부터 LG 베스트샵
- 의견: 그램북 제품군에 14형이 나온 건 처음입니다. 1.3kg 안팎에 61Wh 배터리면 학생용으로 좋은 비율인데, 디스플레이 해상도와 RAM 옵션이 공개된 뒤에 가격을 판단하는 편이 낫겠습니다.
- 출처: [한국경제](https://www.hankyung.com/article/202609015209g), [THE ELEC](https://www.thelec.net/news/articleView.html?idxno=13514)

### 삼성 뉴 갤럭시 북6

- CPU: Intel Core Series 3
- 디스플레이: 14형(35.6cm) 단일 사이즈, 그레이 색상만
- 무게: 1.35kg
- 배터리: 최대 25시간 동영상 재생, 30분 충전으로 최대 33%
- 가격: CPU·OS 등 사양에 따라 119만 원부터 149만 원
- 출시: 9월 1일 국내 출시, 삼성스토어·삼성닷컴·오픈마켓
- 의견: 삼성과 LG가 같은 날, 거의 같은 가격대로 출시한 걸 보면 국내 중가 시장이 지금 격전지입니다. 갤럭시 북6가 조금 더 무겁지만, 진입 가격이 낮은 점은 첫 노트북을 사는 분들에게 크게 작용할 겁니다.
- 출처: [머니투데이](https://www.mt.co.kr/tech/2026/09/01/2026090108110731281), [이데일리](https://www.edaily.co.kr/News/Read?newsId=03191446645575856)

## 해외

### NVIDIA Jetson Orin Nano 2

- AI 연산: 78 TOPS
- CPU: 8코어 Arm Cortex-A78
- GPU: Ampere 아키텍처, CUDA 코어 1,536개
- 메모리: 8GB LPDDR5X, 120GB/s
- 전력: 15W~40W 모드
- NVIDIA 발표 기준 이전 세대 대비 추론 성능 2배, 같은 성능에서 전력 40% 절감
- 가격: 확인 필요 (미발표)
- 출시: 8월 25일(현지 시간) 발표, 모듈과 개발자 키트는 2027년 상반기 출하 예정
- 의견: GPU가 여전히 Ampere라서 성능 향상은 새 아키텍처가 아니라 CUDA 코어 증가와 빠른 메모리에서 옵니다. 온디바이스 비전 로봇 기준으로는 8GB 메모리가 다시 한계가 될 겁니다. 최대 40W 모드는 소형 로봇의 전원 레일과 방열을 다시 설계해야 한다는 뜻이니, 기존 25W 예산을 그대로 가정하면 안 됩니다.
- 출처: [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-jetson-orin-nano-2-robotics-computer-to-redefine-entry-level-edge-ai), [Hackster.io](https://www.hackster.io/news/say-hello-to-the-nvidia-jetson-orin-nano-2-68cf1241460f)
- 자세한 비교와 전력 설계 관점은 [SBC 심층 리뷰: Jetson Orin Nano 2는 무엇이 달라졌나](/2026/09/02/embedded-jetson-orin-nano-2/)에서 따로 다뤘습니다.

### Poco F9 Pro / F9 Ultra

- SoC: Snapdragon 8 Elite Gen 5 (두 모델 공통)
- 디스플레이: 6.59인치(Pro) / 6.9인치(Ultra), 185Hz, 최대 4,500니트, Gorilla Glass 7i
- 카메라: 200MP 메인(OIS), 32MP 전면
- 배터리: 6,330mAh(Pro) / 8,050mAh(Ultra), 100W 유선, 50W 무선
- IP68, Bose 튜닝 스피커
- 가격: F9 Pro 699달러부터(12GB/256GB), F9 Ultra 799달러부터. 영국 799파운드/899파운드. 유로 가격은 출처마다 달라(799/999유로 vs 899.90/1,099.90유로) 확인 필요. 인도 가격 확인 필요
- 출시: 9월 1일 글로벌 발표
- 의견: 8,050mAh 배터리에 100W 충전을 넣은 게 핵심입니다. 다만 가격 인상 폭이 크고, 같은 칩을 쓴 경쟁 제품이 여럿이라 작년만큼 가성비 이야기가 강하지 않습니다.
- 출처: [9to5Google](https://9to5google.com/2026/09/01/poco-f9-pro-and-f9-ultra-launch/), [Tech Advisor](https://www.techadvisor.com/article/3224419/xiaomi-poco-f9-ultra-f9-pro-launch-with-major-price-hikes.html)

## 소프트웨어

### Pollen Robotics microduck

Hugging Face 산하 Pollen Robotics가 25cm, 800g짜리 이족 보행 오리 로봇 microduck의 소프트웨어 스택을 공개했습니다. 강화학습 정책으로 걷고, 구르고, 부리로 물건을 집습니다. 8월 28일 발표 뒤 이번 주 GitHub에서 인기 저장소로 올라왔습니다.

- 저장소: github.com/pollen-robotics/microduck, Apache-2.0, Rust, 작성 시점 약 6.3k 스타
- Rockchip RK3566 보드에서 50Hz 제어 루프로 서보 15개 구동, 카메라·ToF 깊이 센서·Bluetooth·게임패드 지원
- 시뮬레이션과 RL 학습 환경은 별도 저장소 microduck_rl
- 설치·실행: README는 한 줄 설치 대신 문서와 `robotctl` CLI를 안내합니다. 로봇 본체는 pollen-robotics.com/microduck에서 판매
- 의견: 교육용으로 볼 만한 건 오리가 아니라 파이프라인입니다. 시뮬레이션에서 보행을 학습시키고 저가 ARM 보드에 올려 반복하는 흐름이 그대로 공개돼 있습니다. 다만 공개된 건 소프트웨어뿐이고 Pollen이 하드웨어를 오픈소스라 부르지 말아 달라고 밝혔으니 STL 파일은 기대하지 않는 게 좋습니다.
- 출처: [GitHub](https://github.com/pollen-robotics/microduck), [CNX Software](https://www.cnx-software.com/2026/08/28/microduck-a-duck-like-biped-robot-designed-for-physical-ai-experimentation-and-fun/)

## 이번 주 요약

| 제품 | 카테고리 | 지역 | 핵심 스펙 | 가격 | 출시일 |
|---|---|---|---|---|---|
| LG 그램북 AI 2026 14형 | 노트북 | 국내 | Core Series 3, 61.2Wh, 1.29kg | 145만 원부터 | 9월 7일 |
| 삼성 뉴 갤럭시 북6 | 노트북 | 국내 | Core Series 3, 14형, 1.35kg | 119만~149만 원 | 9월 1일 |
| NVIDIA Jetson Orin Nano 2 | SBC/로봇 | 해외 | 78 TOPS, 8코어 A78, 8GB LPDDR5X | 확인 필요 | 2027년 상반기 |
| Poco F9 Pro / F9 Ultra | 스마트폰 | 해외 | Snapdragon 8 Elite Gen 5, 185Hz, 6,330/8,050mAh | 699/799달러부터 | 9월 1일 |
| Pollen Robotics microduck | 오픈소스 | 소프트웨어 | Rust, RK3566, 서보 15개, RL 정책 | Apache-2.0 | 8월 28일 |
