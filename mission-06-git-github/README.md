# Mission 06 — Git and GitHub

## Goal

Understand how Git tracks changes, practise working on a separate branch, and get that work into `main` through a pull request on GitHub.

## Task 6.1 — The Git workflow

```text
 working folder  --git add-->  staging area  --git commit-->  local repo  --git push-->  GitHub
 (files I edit)                (changes picked              (saved history      (online copy)
                                for the next commit)         on my Mac)
                                                    <--git pull--
```

| Command | What it does |
|---|---|
| `git init` | Turns a folder into a Git repository |
| `git status` | Shows what's changed and what's staged |
| `git add <file>` | Puts a change in the staging area |
| `git commit -m "msg"` | Saves the staged changes as a snapshot |
| `git log --oneline` | Lists past commits, one per line |
| `git branch` | Lists branches (`*` marks the current one) |
| `git switch -c <name>` | Creates a new branch and moves onto it |
| `git push` | Sends my commits to GitHub |
| `git pull` | Brings down commits from GitHub |

## Task 6.2 — Working on a branch

**1. Check the branches I have**

```text
$ git branch
* main
```

**2. Make a new branch for my change**

```text
$ git switch -c add-about-me
Switched to a new branch 'add-about-me'
```

**3. Confirm I'm on it**

```text
$ git branch --show-current
add-about-me
```

**4. Make the change.** I added an **About me** section to the top of the root [`README.md`](../README.md), with a short intro and my setup (Mac model, macOS, Python, Git versions).

**5. Stage and commit**

```text
$ git add README.md
$ git commit -m "Add About me section to root README"
```

**6. Push the branch to GitHub**

```text
$ git push -u origin add-about-me
```

At this point `main` didn't have the change yet. It only existed on `add-about-me`.

## Task 6.3 — Pull request

A **pull request (PR)** asks to merge the changes from one branch into another. It shows exactly what changed, line by line, so someone can review it before it reaches `main`.

**Why PRs matter:**
- Mistakes get caught before they reach the main version.
- Teammates can comment on specific lines.
- There's a permanent record of what changed and why.
- `main` always stays in a working state.

**My pull request:** [#1 — Add About me section to root README](https://github.com/anshgandhi68-sys/digital-detective-8009-/pull/1)

| Detail | Value |
|---|---|
| Direction | `add-about-me` → `main` |
| Title | Add About me section to root README |
| Files changed | 1 (`README.md`) |
| Status | **Merged** on 24 Nov 2026 |
| Branch after merge | Deleted (it's not needed once merged) |

After merging, I switched back to `main` and pulled:

```text
$ git switch main
$ git pull
$ git log --oneline --graph
*   7c66839 Merge pull request #1 from anshgandhi68-sys/add-about-me
|\
| * 4e476c9 Add About me section to root README
|/
* 05cef00 Complete Mission 05: manual conversions, number converter, text encoding
```

The graph shows the branch splitting off from `main` and joining back in with a merge commit.

## Task 6.4 — Glossary

| Term | Meaning |
|---|---|
| Repository (repo) | A project folder whose history Git tracks |
| Commit | A saved snapshot of the files, with a message |
| Staging area | Where changes wait before they're committed |
| Branch | A separate line of work that doesn't affect `main` until merged |
| `main` | The default branch, the "official" version |
| Remote / `origin` | The copy of the repo on GitHub |
| Push | Upload local commits to the remote |
| Pull | Download and merge commits from the remote |
| Clone | Download a full copy of a repo from GitHub |
| Fork | Your own copy of someone else's repo on GitHub |
| Pull request | A request to merge one branch into another, with review |
| Merge | Combine the changes from one branch into another |
| Merge conflict | When two branches change the same lines and Git needs a human to choose |
| `.gitignore` | A list of files Git should never track |

## Tools used

Git 2.54.0 in the Terminal, GitHub (website), GitHub CLI (`gh`) to open the PR, VS Code to edit the README

## What I understood

A branch is like a safe copy where I can try things out. While I worked on `add-about-me`, `main` was untouched, so if my change had been bad I could just delete the branch.

The pull request is where the branch gets checked before it's accepted. On my own project I approved it myself, but in a team someone else would review it first. That's how big projects stay stable even with lots of people working on them.

Seeing `git log --graph` after the merge helped me picture it: history isn't always a straight line, it can split off and join back.

## Problems I ran into

- **Problem:** After merging on GitHub, my Mac still showed the old README.
  **Fix:** The merge happened on GitHub, not on my computer. `git switch main` and then `git pull` brought it down.
- **Problem:** `git branch -a` still listed `remotes/origin/add-about-me` after I'd deleted the branch on GitHub.
  **Fix:** `git fetch --prune` cleared out references to branches that no longer exist on GitHub.

## Evidence

- Pull request: https://github.com/anshgandhi68-sys/digital-detective-8009-/pull/1
- Commit history: https://github.com/anshgandhi68-sys/digital-detective-8009-/commits/main
