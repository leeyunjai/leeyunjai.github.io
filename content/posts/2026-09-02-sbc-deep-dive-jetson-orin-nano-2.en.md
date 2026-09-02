---
title: "SBC Deep Dive: What Actually Changed in the Jetson Orin Nano 2"
date: 2026-09-02T17:40:00+09:00
slug: "sbc-deep-dive-jetson-orin-nano-2"
summary: "NVIDIA's next entry-level Jetson compared against the current Orin Nano Super, with a look at the power envelope and memory ceiling that decide whether it fits a robot."
tags: ["SBC", "Robot", "Global"]
categories: ["Deep Dive"]
draft: false
---

NVIDIA announced the Jetson Orin Nano 2 on August 25, with the module and developer kit expected in the first half of 2027. The headline is "2x inference performance," which reads like a generational jump. Line up the specs against the board it replaces and the picture is more specific than that, and the numbers that matter for a robot build are not the ones in the headline.

## Side by side

| | Orin Nano 2 (new) | Orin Nano Super (current) |
|---|---|---|
| AI compute | 78 TOPS | 67 TOPS |
| GPU | Ampere, 1,536 CUDA cores | Ampere, 1,024 CUDA cores + 32 tensor cores |
| CPU | 8-core Arm Cortex-A78 | 6-core Arm Cortex-A78AE |
| Memory | 8 GB LPDDR5X, 120 GB/s | 8 GB 128-bit LPDDR5, 102 GB/s |
| Power | 15 W to 40 W | 7 W to 25 W |
| Price | TBC (not announced) | $249 developer kit |
| Availability | H1 2027 | Shipping now |

Sources: [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-jetson-orin-nano-2-robotics-computer-to-redefine-entry-level-edge-ai), [Hackster.io](https://www.hackster.io/news/say-hello-to-the-nvidia-jetson-orin-nano-2-68cf1241460f), [NVIDIA Jetson Orin Nano Super Developer Kit](https://www.sparkfun.com/nvidia-jetson-orin-nano-developer-kit.html)

## The "2x" is not measured at equal power

Start here, because it changes how you read everything else. On paper the TOPS figure moves from 67 to 78, about 16%. The doubling claim comes from a different comparison: the new board in its 40 W mode against the old board at its 25 W ceiling. It is not twice the performance at the same power draw.

NVIDIA's other claim is the more useful one: 40% lower power at equivalent performance. Put together, the new module gives you more when you feed it more, and costs less when you ask for the same. That also tells you what did not happen. The GPU is still Ampere. The gains come from 50% more CUDA cores, two extra CPU cores, and 18% more memory bandwidth, not from a new architecture.

## The power floor is the part that bites

This is the quietest row in the table and the one most likely to break a design. The envelope moves from 7-25 W to 15-40 W. The ceiling going up is expected. The floor doubling, from 7 W to 15 W, is the problem.

If you have built a battery-powered mobile robot, you already know why. Idle and low-load draw sets your runtime as much as peak draw does. A design that keeps a camera alive and only runs inference on an event spends most of its life near the floor. Swapping in the new module doubles that baseline, and the battery budget you sized for the old board no longer holds.

The 40 W ceiling deserves the same caution from the other direction. You cannot drop this module into a power section designed around 25 W and call it done: rail capacity, connector ratings, and thermal design all need to be recalculated. The module's input voltage and connector pinout have not been published yet, so treat those as TBC until the datasheet lands. Guessing at a power section is how boards get cooked.

## Memory stays at 8 GB

Both generations ship 8 GB. Bandwidth improves from 102 to 120 GB/s, but capacity does not move. Run vision models on-device for a while and you find the wall is usually memory, not compute. Jetson shares memory between CPU and GPU, so after the OS and the camera pipeline take their share, what is actually available to a model is well under 8 GB.

If the plan is to quantize a current vision-language model and run it at the edge, this generation hits the same wall as the last one. Memory fills before you get anywhere near 78 TOPS. More capacity means moving up to something like Orin NX, which is a different price bracket and a different conversation.

## What to buy right now

Shipping is H1 2027. That is more than six months out, with no announced price. **If you have to ship something in 2026, this board is not on the table.**

- **Building now**: the Orin Nano Super developer kit is $249, it is not short on performance, and you can buy it today. Its 7 W floor is also friendlier to battery-powered work than the new board's 15 W.
- **Targeting production in 2027 or later**: plan around the new module, but design the power section and cooling for 40 W from the start. Adding headroom later costs far more than building it in.
- **Learning or teaching**: no reason to wait. The 8 GB ceiling is the same on both, and what you learn transfers when the board changes.

## Verdict

Honestly read, this is a widened Ampere part rather than a new generation: more cores, a broader power envelope, faster memory. That is a perfectly good product. The risk is taking the "2x" line at face value and carrying it into a design, because the place it will hurt you is power. Work out whether your enclosure can actually deliver 40 W, and whether your battery can live with a 15 W floor, before anything else.

Worth revisiting once pricing and the full module datasheet are published.
