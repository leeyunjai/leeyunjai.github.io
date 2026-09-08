---
title: "유즈키네코, 피코 크기에 리눅스 두뇌"
date: 2026-09-09T03:20:00+09:00
slug: "embedded-yuzukineko-risc-v-pico"
summary: "라즈베리파이 피코와 똑같은 크기에 리눅스가 도는 오픈 하드웨어 RISC-V 보드 유즈키네코를 살펴보고, 마이크로컨트롤러인 피코 2와 무엇이 다른지 비교했습니다."
tags: ["SBC", "Global"]
categories: ["Deep Dive"]
cover:
  image: "/images/posts/embedded-yuzukineko-risc-v-pico.ko.png"
  alt: "커버 카드: PSRAM 16MiB, 클록 1.008GHz, 플래시 16MiB, 가격 미정"
  relative: false
draft: false
---

CNX Software가 9월 8일 소개한 유즈키네코(YuzukiNeko)는 라즈베리파이 피코와 똑같은 2×20핀 폼팩터에
리눅스가 도는 애플리케이션 프로세서를 얹은 오픈 하드웨어 보드입니다. 피코 크기 보드는 지금까지
마이크로컨트롤러 전용이었는데, 이 보드는 그 틀을 깨고 디스플레이·영상 처리까지 붙였습니다.

## 유즈키네코

| 항목 | 사양 |
|---|---|
| SoC | Allwinner F101S3, XuanTie C907 RISC-V 코어 1개 |
| 클록 | 1.008GHz |
| 메모리 | PSRAM 16MiB |
| 저장장치 | 외장 NOR 플래시 16MiB(XIP 지원) + microSD 슬롯 |
| 커넥터 | USB-C, FEL 버튼, 2×20핀 피코 스타일 헤더 2조 |
| 디스플레이 | RGB888, LVDS, 4레인 MIPI DSI |
| 영상 처리 | JPEG/PNG 디코드, JPEG/MJPEG 인코드 |
| 오디오 | DAC, I2S/PCM, OWA 출력 |
| OS | Linux, Zephyr RTOS |
| 라이선스 | 하드웨어 설계 CC0 1.0(퍼블릭 도메인) 공개 |
| 가격·출시 | 미정. 아직 판매 시작 전(확인 필요) |

F101S3 SoC 자체는 원래 디스플레이·오디오 응용을 겨냥한 "스마트 컨트롤·디스플레이 프로세서"입니다.
그런데 여기에 PSRAM과 NOR 플래시를 붙이고 리눅스를 올리면서, 피코 폼팩터에서 마이크로컨트롤러가
아니라 진짜 애플리케이션 프로세서를 쓸 수 있게 됐습니다.

### 임베디드 관점

- **메모리 한계**: PSRAM 16MiB는 리눅스를 띄우기엔 빠듯한 용량입니다. 데스크톱 배포판이 아니라
  Buildroot나 OpenWRT 계열의 최소 구성을 올리는 용도에 가깝습니다.
- **전원**: USB-C로 전력을 받는 것은 확인되지만, 정확한 입력 전압·전류 범위는 공개 자료에 없습니다
  (확인 필요). 발열 관련 수치도 아직 공개되지 않았습니다.
- **커넥터**: 2×20핀 헤더 2조가 있어 피코용으로 설계된 캐리어 보드에 그대로 꽂을 수 있을 가능성이
  있지만, 핀 배열이 RP2040/RP2350과 동일한지는 공식 확인이 필요합니다.
- **로봇·장비 탑재 시**: MIPI DSI와 영상 디코드 기능이 있어 소형 디스플레이가 붙은 상태 표시 모듈이나
  간단한 카메라 프리뷰 용도로는 쓸 수 있지만, 실시간 제어처럼 결정론적 응답이 필요한 자리에는
  단일 코어 리눅스보다 마이크로컨트롤러 쪽이 여전히 유리합니다.

## 유즈키네코 vs 라즈베리파이 피코 2

같은 크기, 다른 성격의 보드를 나란히 놓으면 차이가 분명해집니다.

| 항목 | 유즈키네코 | 라즈베리파이 피코 2 |
|---|---|---|
| 폼팩터 | 피코 스타일 2×20핀 | 피코 스타일 2×20핀 |
| CPU | XuanTie C907 RISC-V 1개, 1.008GHz | Cortex-M33 + Hazard3 RISC-V 각 2개, 150MHz |
| 메모리 | PSRAM 16MiB | 온칩 SRAM 520KiB |
| 내장 저장장치 | 외장 NOR 플래시 16MiB | 온보드 플래시 4MB |
| 디스플레이 출력 | RGB888 / LVDS / MIPI DSI | 없음 |
| 실행 환경 | Linux, Zephyr RTOS | 베어메탈, MicroPython, CircuitPython |
| 가격 | 미정 | 5달러(확정, 상시 구매 가능) |

![유즈키네코는 라즈베리파이 피코 2보다 메모리가 약 32배, 내장 저장장치가 4배 많습니다](/images/posts/embedded-yuzukineko-risc-v-pico.ko-compare.png "표를 막대로 그린 것입니다. 메모리 종류(PSRAM vs SRAM)가 다르다는 점은 감안해서 보세요.")

메모리 용량만 보면 유즈키네코가 압도적으로 많지만, 종류가 다릅니다(PSRAM vs 온칩 SRAM). 그리고
피코 2의 150MHz 듀얼 코어는 실시간 제어에 최적화된 마이크로컨트롤러이고, 유즈키네코의 1.008GHz
단일 코어는 리눅스를 돌리기 위한 애플리케이션 프로세서라서 클록만으로 우열을 가릴 수 없습니다.
용도 자체가 다른 보드입니다.

## 장단점과 어떤 사용자에게 맞는가

**장점**: 피코 크기에서 리눅스와 디스플레이 출력을 동시에 쓸 수 있다는 점이 유일합니다. 하드웨어
설계도 CC0로 완전히 공개돼 있어 파생 보드를 만들기도 자유롭습니다.

**단점**: 아직 판매 전 단계라 가격·구매 경로·전원 사양이 확인되지 않았습니다. PSRAM 기반 메모리라
동작 신뢰성이나 실사용 속도는 실물이 나와야 검증됩니다.

**추천 대상**: 피코 폼팩터를 유지한 채 작은 디스플레이나 카메라 프리뷰가 필요한 DIY·메이커 프로젝트,
그리고 오픈 하드웨어 RISC-V 설계를 직접 들여다보고 싶은 임베디드 개발자에게 맞습니다. 실시간 제어가
핵심인 로봇 액추에이터 자리에는 여전히 피코 2 같은 마이크로컨트롤러가 낫습니다.

## 국내 출시 여부

오픈 하드웨어 프로젝트로 공개됐을 뿐 정식 유통·국내 출시 계획은 확인되지 않았습니다(확인 필요).
공식 판매가 시작되면 알리익스프레스 등 해외 직구 경로로 우선 구할 수 있을 가능성이 높습니다.

## 총평

유즈키네코는 "피코 크기 = 마이크로컨트롤러"라는 공식을 깬 첫 사례에 가깝습니다. 다만 아직 가격도
전원 사양도 공개되지 않은 프로토타입 단계라, 실물이 나와 PSRAM 리눅스가 실제로 안정적으로 도는지
확인하는 것이 다음 단계입니다.

**출처**: [CNX Software, 2026-09-08](https://www.cnx-software.com/2026/09/08/yuzukineko-a-linux-capable-allwinner-f101-64-bit-risc-v-sbc-with-raspberry-pi-pico-form-factor/),
[Open Source For You, 2026-09](https://www.opensourceforu.com/2026/09/yuzukineko-brings-open-hardware-to-a-pico-sized-risc-v-board/),
[Raspberry Pi 공식 발표 - Pico 2](https://www.raspberrypi.com/news/raspberry-pi-pico-2-our-new-5-microcontroller-board-on-sale-now/)
