---
title: "On sale today, shipping next year"
date: 2026-09-02T15:00:00+09:00
slug: "brief-weekly-gadgets"
summary: "Two budget 14-inch laptops launched in Korea on the same day, NVIDIA's next entry-level Jetson for robots, and Poco's pricier F9 flagships."
tags: ["Laptop", "SBC", "Smartphone", "GitHub", "Korea", "Global"]
categories: ["Weekly Brief"]
cover:
  image: "/images/posts/brief-weekly-gadgets.en.png"
  alt: "This week in brief: gram Book AI 14, New Galaxy Book6, Jetson Orin Nano 2, Poco F9 Pro"
  relative: false
draft: false
---

The first week of September sits in the calm before two big dates: Apple's September 9 event and IFA Berlin, which opens on September 4. Even so, four products stood out this week. In Korea, LG and Samsung launched budget 14-inch laptops on the same day, which tells you where the domestic PC fight has moved. Overseas, NVIDIA refreshed its entry-level Jetson for robotics, and Poco launched the F9 series with a price increase that is hard to ignore.

## Korea

### LG gram Book AI 2026 14 (14U40V)

LG's gram line has always been about weight, and the gram Book sub-brand is its cheaper, thicker sibling. This is the first time the gram Book line gets a 14-inch model.

- CPU: Intel Core Series 3 (Wildcat Lake)
- Battery: 61.2 Wh, up to 30.5 hours by LG's own measurement
- Weight / thickness: 1.29 kg / 14.9 mm, aluminum chassis
- Display: 14-inch. Resolution and panel type: TBC
- Memory / storage: TBC (varies by configuration)
- Price: from 1,450,000 KRW (MSRP)
- Release: announced Sep 1; on sale Sep 7 at LGE.com and major online malls, with LG Best Shop stores following from mid-September
- Take: 1.29 kg with a 61 Wh pack is a strong ratio for a student machine, and Wildcat Lake should help idle power. But LG has not yet published the display resolution or RAM tiers, so I would hold off on judging the price until the full spec sheet is out.
- Source: [The Korea Economic Daily](https://www.hankyung.com/article/202609015209g), [THE ELEC](https://www.thelec.net/news/articleView.html?idxno=13514)

### Samsung New Galaxy Book6

Samsung's answer landed the same morning. The "New" Galaxy Book6 is a single-size, single-color budget model aimed at students heading back to school.

- CPU: Intel Core Series 3
- Display: 14-inch (35.6 cm), one size, Gray only
- Weight: 1.35 kg
- Battery: up to 25 hours of video playback; a 30-minute charge restores up to 33%
- Price: 1,190,000 to 1,490,000 KRW depending on CPU and OS choice
- Release: Sep 1 in Korea, through Samsung Stores, Samsung.com, and open-market retailers
- Take: Two Korean giants launching on the same day, in almost the same price band, means the mid-range market is now the main battleground at home. The Galaxy Book6 is 60 grams heavier than the gram Book, but its lower entry price will matter more to first-time buyers than the weight difference.
- Source: [Money Today](https://www.mt.co.kr/tech/2026/09/01/2026090108110731281), [Edaily](https://www.edaily.co.kr/News/Read?newsId=03191446645575856)

## Global

### NVIDIA Jetson Orin Nano 2

NVIDIA's entry-level Jetson has been the default brain for hobby and education robots since the Orin Nano Super price cut. The Orin Nano 2 keeps the same tier but changes the silicon underneath.

- AI compute: 78 TOPS
- CPU: 8-core Arm Cortex-A78
- GPU: Ampere architecture, 1,536 CUDA cores
- Memory: 8 GB LPDDR5X at 120 GB/s
- Power: 15 W to 40 W modes
- NVIDIA claims 2x inference performance over the previous generation, and 40% lower power at the same performance level
- Price: TBC (not announced)
- Release: announced Aug 25 (US time); the module and developer kit are expected in the first half of 2027
- Take: The GPU is still Ampere, so the gain comes from more CUDA cores, two extra CPU cores, and faster memory rather than a new architecture. For an on-device vision robot, 8 GB of shared memory is once again the real ceiling. The new 40 W top mode is the part that affects hardware design: a small robot built around the old 25 W budget needs its power rail and cooling rethought before this module goes in. And with shipping a good six months away, nobody should plan a 2026 build around it.
- Source: [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-jetson-orin-nano-2-robotics-computer-to-redefine-entry-level-edge-ai), [Hackster.io](https://www.hackster.io/news/say-hello-to-the-nvidia-jetson-orin-nano-2-68cf1241460f)
- Going deeper: [SBC Deep Dive: What Actually Changed in the Jetson Orin Nano 2](/en/2026/09/02/embedded-jetson-orin-nano-2/) covers the comparison and the power-design side.

### Poco F9 Pro and F9 Ultra

Poco built its name on flagship chips at mid-range prices. The F9 series keeps the flagship chip but moves the price up a tier.

- SoC: Snapdragon 8 Elite Gen 5 on both models
- Display: 6.59-inch (Pro) / 6.9-inch (Ultra), 185 Hz, 4,500 nits peak, Gorilla Glass 7i
- Camera: 200 MP main with OIS, 32 MP front
- Battery: 6,330 mAh (Pro) / 8,050 mAh (Ultra), 100 W wired and 50 W wireless charging
- IP68 rating, Bose-tuned speakers
- Price: F9 Pro from $699 (12 GB / 256 GB), F9 Ultra from $799; UK £799 / £899. Euro pricing differs between sources (€799 / €999 versus €899.90 / €1,099.90): TBC. India pricing: TBC
- Release: global launch Sep 1
- Take: An 8,050 mAh cell with 100 W charging in a phone body is the headline, and the 185 Hz panel is a spec nobody asked for but gamers will like. The problem is price. Poco itself blamed rising memory costs, but with the same chip as several rivals, the value story that defined the F series is much weaker this year.
- Source: [9to5Google](https://9to5google.com/2026/09/01/poco-f9-pro-and-f9-ultra-launch/), [Tech Advisor](https://www.techadvisor.com/article/3224419/xiaomi-poco-f9-ultra-f9-pro-launch-with-major-price-hikes.html)

## Software

### Pollen Robotics microduck

Pollen Robotics, now part of Hugging Face, published the software stack for microduck, a 25 cm, 800 g biped duck robot that walks, rolls, and grasps using reinforcement-learning policies. The repository trended on GitHub this week after the August 28 announcement.

- Repo: github.com/pollen-robotics/microduck, Apache-2.0, Rust, about 6.3k stars at the time of writing
- Runs on a Rockchip RK3566 board with a 50 Hz control loop driving 15 servos, plus camera, ToF depth sensor, Bluetooth, and gamepad support
- Companion repo microduck_rl holds the simulation and RL training environments
- Install or run: the README points to the documentation and a `robotctl` command-line tool rather than a one-line install; the robot itself is sold at pollen-robotics.com/microduck
- Take: The interesting part for education is the pipeline, not the duck: train a gait in simulation, deploy to a cheap ARM board, iterate. Note that only the software is open; Pollen has asked press not to call the hardware open source, so do not expect STL files.
- Source: [GitHub](https://github.com/pollen-robotics/microduck), [CNX Software](https://www.cnx-software.com/2026/08/28/microduck-a-duck-like-biped-robot-designed-for-physical-ai-experimentation-and-fun/)

## This Week at a Glance

| Product | Category | Region | Key specs | Price | Release |
|---|---|---|---|---|---|
| LG gram Book AI 2026 14 | Laptop | Korea | Core Series 3, 61.2 Wh, 1.29 kg | from 1,450,000 KRW | Sep 7 |
| Samsung New Galaxy Book6 | Laptop | Korea | Core Series 3, 14-inch, 1.35 kg | 1,190,000 to 1,490,000 KRW | Sep 1 |
| NVIDIA Jetson Orin Nano 2 | SBC / Robotics | Global | 78 TOPS, 8-core A78, 8 GB LPDDR5X | TBC | H1 2027 |
| Poco F9 Pro / F9 Ultra | Smartphone | Global | Snapdragon 8 Elite Gen 5, 185 Hz, 6,330 / 8,050 mAh | from $699 / $799 | Sep 1 |
| Pollen Robotics microduck | Open source | Software | Rust, RK3566, 15 servos, RL policies | Apache-2.0 | Aug 28 |
