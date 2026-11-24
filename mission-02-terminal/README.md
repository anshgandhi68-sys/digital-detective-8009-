# Mission 02 — Terminal

## Goal

Get comfortable using the Terminal instead of Finder: move around folders, create and change files safely, use flags and pipes, and find out what a package manager is.

All the commands below were run in the macOS Terminal (zsh) on my MacBook Pro. The practice files are in [`terminal-practice/`](terminal-practice/).

## Task 2.1 — Moving around

| Command | What it did for me |
|---|---|
| `pwd` | Printed where I am: `/Users/anshgandhi/digital-detactive-8009/mission-02-terminal` |
| `ls` | Listed the files in the current folder |
| `cd terminal-practice` | Moved into the practice folder |
| `cd ..` | Went back up one level |
| `cd` (on its own) | Took me straight to my home folder `/Users/anshgandhi` |
| `mkdir terminal-practice` | Created a new folder |

## Task 2.2 — Making changes safely

I did all the file experiments inside `terminal-practice/` so I couldn't accidentally damage anything else.

```text
$ touch todo.txt                                   # make an empty file
$ echo "Mission 02 practice file - Ansh" > todo.txt  # > replaces the contents
$ echo "Learnt: pwd, ls, cd, mkdir" >> todo.txt      # >> adds to the end
$ cat todo.txt
Mission 02 practice file - Ansh
Learnt: pwd, ls, cd, mkdir

$ cp todo.txt todo-backup.txt      # copy
$ mv todo-backup.txt todo-old.txt  # rename
$ mkdir old
$ mv todo-old.txt old/             # move into a folder

$ ls -R
old
todo.txt

./old:
todo-old.txt
```

**Safety rules I followed:**
- Run `pwd` before doing anything destructive, to be sure I'm in the right folder.
- Make a copy with `cp` before changing an important file.
- Be careful with `>`: it wipes the file before writing. `>>` is the safe one for adding.
- I didn't use `rm -rf`. Terminal has no Trash, so a deleted file is gone for good.

## Task 2.3 — Flags and pipes

A **flag** changes how a command behaves. A **pipe** (`|`) sends one command's output into another command.

| Command | What changed |
|---|---|
| `ls` | Just names |
| `ls -a` | Also shows hidden files that start with `.` (like `.gitignore`) |
| `ls -l` | Long format: permissions, owner, size, date |
| `ls -lh` | Same, but sizes are human-readable (`59B` instead of `59`) |
| `ls -lah` | All three flags together |

```text
$ ls -lh terminal-practice
drwxr-xr-x@ 3 anshgandhi  staff    96B Nov 25 01:01 old
-rw-r--r--@ 1 anshgandhi  staff    59B Nov 25 01:01 todo.txt
```

Pipes I tried:

```text
$ ls -lah ~ | head -n 5      # only the first 5 lines of my home folder listing
$ ls /Applications | wc -l   # count my apps
      33
$ ls /Applications | grep -i code   # search the list
Visual Studio Code.app
```

## Task 2.4 — Package managers

A package manager installs, updates and removes command-line tools for you, and also installs whatever other tools they depend on. It's like an App Store for the Terminal. On macOS the usual one is **Homebrew**.

```text
$ brew --version
Homebrew 7.0.15
$ brew list | wc -l
      77
```

So I have 77 packages installed through Homebrew. Most of them are dependencies that got pulled in automatically, like `ca-certificates` and `brotli`.

| Platform | Package manager |
|---|---|
| macOS | Homebrew (`brew`) |
| Ubuntu/Debian Linux | `apt` |
| Python libraries | `pip` |
| JavaScript libraries | `npm` |

## Commands used

`pwd`, `ls`, `ls -a`, `ls -l`, `ls -lh`, `ls -lah`, `ls -R`, `cd`, `cd ..`, `mkdir`, `touch`, `echo`, `>`, `>>`, `cat`, `cp`, `mv`, `head`, `wc -l`, `grep`, `|`, `brew --version`, `brew list`

## What I understood

The Terminal does the same things as Finder, just by typing instead of clicking. Once you know the commands it's often quicker: `ls /Applications | grep -i code` finds an app in one line, and Finder can't count files the way `wc -l` does.

Pipes were the most interesting part. Each command does one small job, and `|` lets me chain them together to make something bigger. Flags work in a similar way: one command like `ls` can behave differently depending on the letters I add.

I also learnt that the Terminal doesn't ask "are you sure?" the way Finder does, so habits like checking `pwd` and keeping practice files in their own folder actually matter.

## Problems I ran into

- **Problem:** At first I mixed up `>` and `>>`, and the second `echo` replaced my first line instead of adding to it.
  **Fix:** I ran `cat` after each step to check the file, and redid it with `>>`.
- **Problem:** `ls` didn't show `.gitignore`, so I thought the file was missing.
  **Fix:** Files starting with `.` are hidden. `ls -a` shows them.

## Evidence

- [`terminal-practice/todo.txt`](terminal-practice/todo.txt) and [`terminal-practice/old/todo-old.txt`](terminal-practice/old/todo-old.txt), the files created in Task 2.2
- Terminal output is copied into the code blocks above
