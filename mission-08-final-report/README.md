# Mission 08 — Final Report

## Goal

Review the whole repository, check that every mission is complete and every program still runs, confirm the Git history is clean, and get everything ready to submit.

## Repository layout

```text
digital-detactive-8009/
├── README.md                     overview, About me, mission table
├── .gitignore                    keeps .DS_Store, __pycache__ and the compiled C file out
├── evidence/                     raw output saved from my Mac
├── mission-00-setup/             workspace setup, tool versions
├── mission-01-computer-basics/   IPOS, hardware vs software
├── mission-02-terminal/          commands, flags, pipes, Homebrew
│   └── terminal-practice/        files I created and moved around
├── mission-03-operating-system/  processes, paths, permissions
├── mission-04-programs/          hello.py, hello.c, compiler vs interpreter
├── mission-05-numbers-data/      conversions, number_converter.py, ASCII/UTF-8
├── mission-06-git-github/        branch + pull request #1
├── mission-07-networking/        DNS, ping, traceroute, how a website loads
└── mission-08-final-report/      this file
```

## Mission review

| # | Mission | Main thing I did | Done? |
|---|---|---|---|
| 00 | Setup | Created the repo and folders, checked Python 3.14.6 and Git 2.54.0 | ✔ |
| 01 | Computer Basics | Traced IPOS through a GarageBand recording; sorted 10 items as hardware/software | ✔ |
| 02 | Terminal | Created, copied, renamed and moved files in `terminal-practice/`; used flags and pipes | ✔ |
| 03 | Operating System | Counted 920 processes; read and changed permissions; got `permission denied` on purpose | ✔ |
| 04 | Programs | Ran `hello.py`; compiled `hello.c` with clang to compare compiler vs interpreter | ✔ |
| 05 | Numbers and Data | 7 hand conversions, checked in Python; built a 3-way converter; explored ASCII and UTF-8 | ✔ |
| 06 | Git and GitHub | Worked on branch `add-about-me`, opened and merged [PR #1](https://github.com/anshgandhi68-sys/digital-detective-8009-/pull/1) | ✔ |
| 07 | Networking | Ran `nslookup`, `ping`, `traceroute`, `curl`; explained a website loading in 10 steps | ✔ |
| 08 | Final Report | Reviewed everything, re-ran the code, checked links and history | ✔ |

## Root README check

- [x] Has a title with my name
- [x] Has an **About me** section with my setup (added through PR #1)
- [x] Mission table links to all nine mission READMEs, all marked Done
- [x] Shows how to run the two Python programs
- [x] Links to the `evidence/` folder

## Final run of the programs

```text
$ python3 mission-04-programs/hello.py
Hi, I'm Ansh and this is my Digital Detective project.
2026 in binary is 11111101010

$ python3 mission-05-numbers-data/number_converter.py 25
     decimal: 25
      binary: 11001
 hexadecimal: 19

$ python3 mission-05-numbers-data/number_converter.py 0x1F
     decimal: 31
      binary: 11111
 hexadecimal: 1F
```

Both programs still work from the repo root. Full output is in [`evidence/mission-08-checks.txt`](../evidence/mission-08-checks.txt).

## Git and GitHub check

```text
$ git status
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean

$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

- One commit per mission, each with a message saying what was done
- The Mission 06 branch was merged through a pull request and then deleted
- Local `main` and GitHub `main` match

## Final checklist

- [x] All nine mission folders have a complete README
- [x] Every README has: goal, work done, commands, what I understood, problems I ran into, evidence
- [x] `hello.py` and `number_converter.py` run without errors
- [x] The number converter handles bad input (`-5`, `abc`) without crashing
- [x] No broken relative links between READMEs
- [x] No `.DS_Store` or compiled files committed
- [x] Private network details partly hidden in Mission 07
- [x] Everything pushed to GitHub

## Problems I ran into

- **Keeping the repo tidy:** macOS kept making `.DS_Store` files and Python made `__pycache__/`. The `.gitignore` from Mission 00 already covered them, and I added the compiled `hello` from Mission 04.
- **Checking links:** With nine READMEs linking to each other and to `evidence/`, it was easy to get a path wrong. I went through every relative link and checked that each file exists.

## What I learnt overall

- **How a computer works:** every system, from my laptop to a lift, follows input → processing → output → storage.
- **The Terminal:** I can now move around, manage files, and chain commands with pipes, often faster than in Finder.
- **The operating system:** macOS is a manager that shares the CPU, RAM and files between about 900 processes and enforces permissions.
- **How code runs:** compiled languages (C) become machine code first; interpreted ones (Python) are run line by line.
- **Data:** numbers and text are all binary underneath, and hex and UTF-8 are agreed ways of writing them.
- **Git and GitHub:** commits, branches and pull requests let me save history, experiment safely, and review changes before they're accepted.
- **Networking:** loading a website goes through DNS, my router, my provider, many internet routers, TCP, TLS and HTTP, usually in under a second.

The biggest change for me is that I stopped treating my computer as a black box. I now have commands I can run to see what's actually going on inside it.

## Submission details

| | |
|---|---|
| Student | Ansh Gandhi |
| GitHub repository | https://github.com/anshgandhi68-sys/digital-detective-8009- |
| Pull request (Mission 06) | https://github.com/anshgandhi68-sys/digital-detective-8009-/pull/1 |
| Computer used | MacBook Pro, Apple M5 Pro, macOS 27.2.1 |
