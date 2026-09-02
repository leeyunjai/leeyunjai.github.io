---
title: "MiniMind Thinks Small, God's Eye Sees Big"
date: 2026-09-03T07:57:31+09:00
slug: "dev-minimind-gods-eye-view"
summary: "This week's GitHub trending list pairs MiniMind, a 64M-parameter language model you can train in two hours, with God's Eye View, a browser-based 3D globe streaming live satellite, flight, and shipping data."
tags: ["GitHub"]
categories: ["Dev Picks"]
draft: false
---

Two repositories climbed GitHub's trending chart this week heading in opposite directions. One shrinks a language model down to something you can train on a single desktop GPU; the other pulls the planet's live data feeds into one browser tab. Here's a closer look at both, picked with on-device AI and developer tooling in mind — the kind of projects worth cloning on a weekend rather than just reading about.

## MiniMind

- Repo: [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
- License: Apache License 2.0
- Language: Python
- Stars: 57,757 (at time of writing), +1,949 this week
- Latest release: minimind-3 / minimind-3-moe (2026-04-01)

MiniMind trains a 64-million-parameter language model from scratch using plain, unwrapped code instead of a heavyweight framework. The README pegs the cost at roughly 3 yuan (about $0.43) and two hours on a single RTX 3090 (24GB). Both the training and inference scripts are short enough to read end to end, which makes this a project for developers who actually want to trace what happens inside a transformer training loop rather than call an API.

```bash
git clone --depth 1 https://github.com/jingyaogong/minimind
cd minimind && pip install -r requirements.txt

# Inference
python eval_llm.py --load_from ./minimind-3

# Training
cd trainer && python train_pretrain.py
cd trainer && python train_full_sft.py
```

On C-Eval and CMMLU the base model scores 24.89% and 25.38% respectively; on English benchmarks (ARC, PIQA, OpenBookQA, HellaSwag, SocialIQA) scores range from roughly 23% to 50% depending on the task, per the README. A LoRA-aligned variant, minimind-3-exam, adds about 2.9 percentage points on top of that. At 64M parameters this isn't production-grade output — it's a teaching tool, best suited to students and engineers who want to build LLM training intuition line by line rather than deploy something.

What makes this worth a look isn't the benchmark numbers, which are modest by design, but the fact that the entire stack — tokenizer, pretraining loop, supervised fine-tuning, and evaluation — fits in a repository small enough to read in an afternoon. Most public LLM training code lives inside large frameworks that hide the actual mechanics behind configuration files and abstraction layers. MiniMind strips that away, so a single RTX 3090 and a couple of hours are enough to watch loss curves move and see exactly which line of code caused it. That tradeoff — clarity over capability — is the whole pitch.

## God's Eye View

- Repo: [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view)
- License: MIT
- Language: JavaScript
- Stars: 16,070, +12,042 this week (the single biggest weekly gain on the trending page)
- Latest release: TBC — the repo ships by commit rather than tagged releases

God's Eye View is a browser-based spatial-intelligence dashboard that layers public real-time data onto a photorealistic 3D globe: aircraft from OpenSky Network and adsb.lol, vessels from AISStream, satellites from CelesTrak, earthquakes from USGS, wildfires from NASA FIRMS, launch schedules from Launch Library 2, city CCTV feeds, and geolocated radio stations. Basemaps come from Cesium ion, Google Maps, Esri, and OpenStreetMap.

```bash
npm install
npm run doctor
npm run dev
# open http://localhost:4173
```

It can also be installed through Pinokio by pasting the repo URL into the Discover tab. This is worth a look for frontend developers who want to build a live tracking dashboard without standing up a dedicated GIS stack, or anyone looking for a side project built entirely on public data APIs. As a pure open-source tool, there's no Korea-specific launch or pricing angle to report here.

The interesting engineering problem here isn't the 3D rendering — Cesium already handles that — it's normalizing a dozen unrelated data sources with different rate limits, coordinate systems, and update frequencies into one coherent scene. A satellite feed from CelesTrak refreshes on a very different cadence than an OpenSky aircraft ping, and the repo's real contribution is the plumbing that keeps all of it in sync without the browser choking. That's also the biggest weekly star gain on this week's entire trending page, ahead of every other repository — a sign that "open data, one screen" is resonating well beyond the GIS niche it started in.

## Wrap-up

These two projects pull in opposite directions but teach a similar lesson. MiniMind shrinks the model so you can actually see the training process; God's Eye View stitches together a dozen public APIs so you can see what's possible when you compose data instead of building it from scratch. Both repos run as-is — clone whichever one matches what you're curious about and try it.
