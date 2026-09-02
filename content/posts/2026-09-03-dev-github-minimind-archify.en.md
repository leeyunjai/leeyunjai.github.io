---
title: "An LLM in two hours, a diagram in one command"
date: 2026-09-03T06:30:10+09:00
slug: "dev-github-minimind-archify"
summary: "Two developer repositories from this week's GitHub trending: MiniMind, which trains a 64M-parameter language model from scratch on one GPU, and Archify, an agent skill that turns a system description into a verifiable architecture diagram. Licenses and install commands included."
tags: ["GitHub", "Global"]
categories: ["Dev Picks"]
draft: false
---

Thursday is dev picks day. From this week's GitHub weekly trending list I pulled two repositories a developer can actually run today. One is about building a language model rather than downloading one; the other turns a written system description into a diagram you can diff. Every command below is copied from the project's README, and anything I could not confirm is marked as such.

Why these two and not the rest of the list? The weekly page is dominated by prompt collections, satellite toys and agent marketplaces. The two below are the ones where you type a command, something concrete happens on your own machine, and you learn a technique you can reuse: how a small model is trained, and how a design document can be generated and verified rather than hand-drawn. I skipped one strong candidate, Mano-P (an on-device GUI agent for Apple Silicon), because its last commit is from late June and it was not on this week's list. It goes back in the queue for when it moves again.

## MiniMind

- Repo: [github.com/jingyaogong/minimind](https://github.com/jingyaogong/minimind)
- License: Apache-2.0 · Language: Python · Stars: about 57.7k (+1.9k this week)
- Latest model release: minimind-3 / minimind-3-moe, 2026-04-01 (per the README)

MiniMind is a framework for training a **64-million-parameter language model from scratch**, end to end. Pretraining, supervised fine-tuning, reinforcement learning (DPO, PPO, GRPO), tool use and knowledge distillation all live in one repository with few dependencies. The point is not the model you get at the end; it is that you read and run every stage, tokenizer to training loop, and come out understanding how an LLM is actually put together.

The README's minimum is a single RTX 3090 (24 GB), about two hours for one SFT epoch, and roughly 3 RMB of cloud compute. From an on-device angle, 64M parameters is small enough to run inference on a Raspberry Pi 5 or a Jetson, so the natural workflow is train on a desktop, deploy to the board.

```bash
git clone --depth 1 https://github.com/jingyaogong/minimind
cd minimind && pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
# try inference with a trained checkpoint
modelscope download --model gongjy/minimind-3 --local_dir ./minimind-3
python eval_llm.py --load_from ./minimind-3
```

The pip mirror flag (`-i ...aliyun...`) is a China-side speed-up you can drop elsewhere. Model weights ship through ModelScope, so you need the `modelscope` package.

- For: developers who want to understand LLM internals in code, and anyone who wants to build a tiny model and put it on an embedded board. Not for people who need a strong model.

## Archify

- Repo: [github.com/tt-a1i/archify](https://github.com/tt-a1i/archify)
- License: MIT · Language: JavaScript/TypeScript (Node.js) · Stars: about 43.7k (**+25.5k this week**, top of the weekly list)
- Release: the releases page shows v2.16.0 as the latest tag while the README references 2.17.0-dev.1; the release page dates read as 2024, which needs confirming

Archify is an agent skill that takes a description of a system and produces **architecture, workflow, sequence, data-flow and lifecycle diagrams as a single self-contained HTML file**. Input is a typed JSON spec, output is validated and deterministic, so design documents can live in git, get diffed, and be compared version to version with the `compare` command. It is built to sit inside coding agents: Cursor, Claude Code, Codex CLI, OpenCode and others.

Twenty-five thousand stars in a week says how much demand there is for letting an agent draw the picture. The release metadata has not kept pace with that growth, which is why the version and date above carry a caveat.

```bash
npx skills add tt-a1i/archify -g
node archify/bin/archify.mjs doctor
node archify/bin/archify.mjs guide "Show CI/CD checks, approval, deploy, and rollback"
node archify/bin/archify.mjs preview workflow examples/agent-tool-call.workflow.json /tmp/workflow.html
```

- For: teams that want design docs treated like code, and developers already using a coding agent who want it to handle documentation too. Not for anyone who wants to draw with a mouse.

## Before you run them

- MiniMind assumes an NVIDIA GPU and a Linux-style shell. On a Mac or a CPU-only box the training path will not fit the two-hour claim; inference on the released checkpoint still works. Weights come from ModelScope, so expect a Chinese CDN and install the `modelscope` package first.
- Archify is a Node.js project installed through the `skills` CLI (`npx skills add`). It expects to be invoked by a coding agent or from the command line; the `doctor` command is the right first call because it reports which integrations it found on your machine.
- Both are moving fast. Star counts and version strings in this post are from the day of writing and will be stale within a week.

## Wrap-up

| Project | License | Language | Stars | This week | In one line |
|---|---|---|---|---|---|
| MiniMind | Apache-2.0 | Python | 57.7k | +1.9k | Train a 64M LLM from scratch on one GPU |
| Archify | MIT | JS/TS | 43.7k | +25.5k | Description in, verifiable diagram HTML out |

Sources: [GitHub Trending (weekly)](https://github.com/trending?since=weekly), each repository's README and releases page. Star counts as of 2026.09.03.
