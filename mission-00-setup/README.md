# Mission 00 — Setting Up My Workspace

## Goal

Get a GitHub repository ready for the assignment, lay out a folder for every mission, and confirm that Python 3 and Git are installed on my Mac.

## What I did

1. Made a project folder on my Mac called `digital-detactive-8009`.
2. Ran `git init` inside it to turn it into a Git repository.
3. Added one folder per mission (`mission-00-setup` through `mission-08-final-report`) plus an `evidence` folder, each with its own `README.md`.
4. Wrote a root `README.md` with a table linking to every mission.
5. Added a `.gitignore` so macOS `.DS_Store` files don't get committed.
6. Checked my Python and Git versions (below).
7. Made my first commit and pushed it to GitHub.

**GitHub repo:** https://github.com/anshgandhi68-sys/digital-detective-8009-

## Tool check

| Command | Output on my Mac |
|---|---|
| `python3 --version` | `Python 3.14.6` |
| `git --version` | `git version 2.54.0 (Apple Git-157)` |

macOS version: 27.2.1

## Commands used

| Command | What it does |
|---|---|
| `mkdir <name>` | Makes a new folder |
| `git init` | Starts tracking a folder with Git |
| `git add .` | Stages every changed file for the next commit |
| `git commit -m "..."` | Saves a snapshot of the staged files |
| `git remote add origin <url>` | Links the local repo to the one on GitHub |
| `git push -u origin main` | Uploads my commits to GitHub |

## What I understood

Git and GitHub are not the same thing. **Git** is a program on my Mac that keeps track of every change I make to the files in a folder. **GitHub** is a website that stores a copy of that Git repository online, so I can back it up, share it, and work on it from other computers.

A **commit** is a saved snapshot of my files at one moment, with a message saying what changed. If I break something later, I can go back to an earlier commit.

I gave each mission its own folder so the work stays separate and easy to find. A teacher can open one folder and see everything for that mission without digging through the others.

## Problems I ran into

- My first `git commit` stopped because Git didn't know my name and email yet. I fixed it with `git config user.name` and `git config user.email`.
- macOS kept creating hidden `.DS_Store` files in every folder. I added them to `.gitignore` so they don't end up on GitHub.

## Checklist

- [x] Project folder created
- [x] Mission folders and READMEs created
- [x] Python version checked
- [x] Git version checked
- [x] First commit pushed to GitHub
- [x] "What I understood" written
- [x] Tool versions saved in [`evidence/mission-00-versions.txt`](../evidence/mission-00-versions.txt)
