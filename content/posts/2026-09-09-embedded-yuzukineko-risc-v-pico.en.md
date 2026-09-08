---
title: "YuzukiNeko, Pico's Size With a Linux Brain"
date: 2026-09-09T03:20:00+09:00
slug: "embedded-yuzukineko-risc-v-pico"
summary: "YuzukiNeko is an open-hardware RISC-V board shaped exactly like a Raspberry Pi Pico, but it runs Linux instead of bare-metal firmware. Here's how it compares to the Pico 2."
tags: ["SBC", "Global"]
categories: ["Deep Dive"]
cover:
  image: "/images/posts/embedded-yuzukineko-risc-v-pico.en.png"
  alt: "Cover card: 16MiB PSRAM, 1.008GHz clock, 16MiB flash, price TBC"
  relative: false
draft: false
---

CNX Software covered YuzukiNeko on September 8, and it's an unusual board: same 2x20-pin
form factor as a Raspberry Pi Pico, but instead of a microcontroller it carries an
application processor that runs Linux. Pico-sized boards have so far been strictly
microcontroller territory. This one breaks that pattern and adds display and video
capability on top.

## YuzukiNeko

| Spec | Detail |
|---|---|
| SoC | Allwinner F101S3, single XuanTie C907 RISC-V core |
| Clock | 1.008GHz |
| Memory | 16MiB PSRAM |
| Storage | 16MiB external NOR flash (XIP-capable) + microSD slot |
| Connectors | USB-C, FEL button, two 2x20-pin Pico-style headers |
| Display | RGB888, LVDS, 4-lane MIPI DSI |
| Video | JPEG/PNG decode, JPEG/MJPEG encode |
| Audio | DAC, I2S/PCM, OWA output |
| OS | Linux, Zephyr RTOS |
| License | Hardware design released under CC0 1.0 (public domain) |
| Price / availability | TBC — not yet on sale (TBC) |

The F101S3 SoC itself was designed as a "smart control and display processor" aimed at
display and audio workloads. Pairing it with PSRAM and NOR flash, then booting Linux on
it, is what turns a Pico-shaped board into a real application processor rather than a
microcontroller.

The CPU core is worth a second look, too. XuanTie C907 comes from T-Head, the chip design
arm behind several of the RISC-V cores already shipping in Allwinner's lineup. Putting one
into a board this small, at this price class, is part of a broader pattern: RISC-V
application cores are trickling down from mid-range SoCs into hobbyist form factors that
used to be exclusively Arm or microcontroller-only. YuzukiNeko is a small but concrete data
point for that trend, not a one-off curiosity.

### The embedded angle

- **Memory ceiling**: 16MiB of PSRAM is tight for Linux. This is Buildroot- or
  OpenWRT-class minimal-userland territory, not a desktop distro.
- **Power**: USB-C is confirmed as the power connector, but the exact input voltage and
  current range aren't published (TBC). No thermal figures are available yet either.
- **Connectors**: two 2x20-pin headers raise the possibility of drop-in compatibility
  with existing Pico carrier boards, but whether the pinout actually matches RP2040/RP2350
  is not officially confirmed.
- **On a robot or piece of equipment**: MIPI DSI and video decode make it plausible for a
  small status display or a simple camera preview, but for deterministic real-time
  control, a microcontroller still beats a single-core Linux board.

## YuzukiNeko vs Raspberry Pi Pico 2

Same footprint, very different character once you put the two side by side.

| Spec | YuzukiNeko | Raspberry Pi Pico 2 |
|---|---|---|
| Form factor | Pico-style 2x20-pin | Pico-style 2x20-pin |
| CPU | 1x XuanTie C907 RISC-V, 1.008GHz | 2x Cortex-M33 + 2x Hazard3 RISC-V, 150MHz |
| Memory | 16MiB PSRAM | 520KiB on-chip SRAM |
| Onboard storage | 16MiB external NOR flash | 4MB onboard flash |
| Display output | RGB888 / LVDS / MIPI DSI | None |
| Runtime | Linux, Zephyr RTOS | Bare metal, MicroPython, CircuitPython |
| Price | TBC | $5 (confirmed, always in stock) |

![YuzukiNeko carries roughly 32x the memory and 4x the onboard storage of the Raspberry Pi Pico 2](/images/posts/embedded-yuzukineko-risc-v-pico.en-compare.png "Bar chart of the table above. Note the memory types differ (PSRAM vs SRAM).")

By raw capacity, YuzukiNeko dwarfs the Pico 2, but the memory types aren't the same
(PSRAM vs. on-chip SRAM). And the Pico 2's 150MHz dual-core setup is a microcontroller
built for deterministic real-time control, while YuzukiNeko's 1.008GHz single core exists
to run Linux — clock speed alone doesn't make one "faster" than the other. These are
different classes of board doing different jobs.

## Pros, cons, and who it's for

**Pros**: it's the only board that puts Linux and display output into a Pico-sized
footprint. The hardware design is fully open under CC0, so derivative boards are free to
build.

**Cons**: it's pre-release, so price, purchase channel, and power specs are all
unconfirmed. Real-world reliability and performance on PSRAM-backed memory still need
verification once hardware ships.

**Who it's for**: maker and DIY projects that want a small display or camera preview
while keeping the Pico footprint, and embedded developers who want to study an open RISC-V
hardware design firsthand. For real-time actuator control on a robot, a microcontroller
like the Pico 2 remains the better fit.

It's also worth flagging who it is *not* for, at least yet. Anyone who needs a bill of
materials, a firm ship date, or a vendor to buy from today should wait — none of that
exists publicly right now. The CC0 release means the schematics and board files can be
picked up and cloned by anyone, which is exactly how a lot of small RISC-V boards from
Chinese SoC vendors reach a wider audience: not through a single official retailer, but
through community fabrication runs once the design settles.

## Korea availability

No Korean distribution or launch plans have surfaced — this is an open-hardware project
release, not a commercial product announcement yet (TBC). Once it goes on sale, overseas
retailers like AliExpress are the most likely first purchase channel.

## Verdict

YuzukiNeko is close to the first board to break the "Pico-sized means microcontroller"
assumption. But it's still a pre-release prototype with no confirmed price or power specs
— the next step is real hardware proving PSRAM-backed Linux actually runs reliably.

**Sources**: [CNX Software, 2026-09-08](https://www.cnx-software.com/2026/09/08/yuzukineko-a-linux-capable-allwinner-f101-64-bit-risc-v-sbc-with-raspberry-pi-pico-form-factor/),
[Open Source For You, 2026-09](https://www.opensourceforu.com/2026/09/yuzukineko-brings-open-hardware-to-a-pico-sized-risc-v-board/),
[Raspberry Pi official announcement - Pico 2](https://www.raspberrypi.com/news/raspberry-pi-pico-2-our-new-5-microcontroller-board-on-sale-now/)
