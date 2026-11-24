# Mission 03 — Operating System

## Goal

Find out what the operating system on my Mac actually does: which OS and kernel I'm running, what processes are, how paths work, and how file permissions protect things.

## Task 3.1 — My operating system

```text
$ sw_vers
ProductName:     macOS
ProductVersion:  27.2.1
BuildVersion:    26B131

$ uname -sr
Darwin 27.2.0

$ uname -m
arm64

$ whoami
anshgandhi
```

| Detail | Value | What it means |
|---|---|---|
| OS | macOS 27.2.1 | The operating system I use every day |
| Kernel | Darwin 27.2.0 | The core of macOS that talks directly to the hardware |
| Architecture | arm64 | My M5 Pro chip uses the ARM instruction set, not Intel's x86 |
| User | `anshgandhi` | The account I'm logged in as. The OS checks this for permissions |

## Task 3.2 — Processes

A **process** is a program that is running right now. Every process gets an ID number (PID).

```text
$ ps aux | wc -l
     920
```

So about **920 processes** were running on my Mac, even though I only had a few apps open. Most are background services that macOS runs for itself.

```text
$ top -l 1 -n 0 | head -5
Processes: 920 total, 2 running, 918 sleeping, 4427 threads
Load Avg: 1.60, 1.61, 1.67
CPU usage: 1.51% user, 6.50% sys, 91.97% idle
PhysMem: 22G used (3289M wired, 1895M compressor), 1265M unused.
```

What I noticed:
- Only **2** processes were actually running at that moment. The other 918 were sleeping, waiting for something to do. The CPU switches between them so fast that it looks like they all run at once.
- The CPU was about **92% idle**.
- The process using the most CPU was `WindowServer`. It's the part of macOS that draws every window on the screen.
- `ps -o pid,ppid,comm -p $$` showed my own Terminal shell (`/bin/zsh`) with its PID and a **PPID**, the parent process that started it. Processes form a family tree.

I also opened **Activity Monitor** (Applications → Utilities), which shows the same information with a graphical interface.

## Task 3.3 — Paths and permissions

### Paths

| Type | Example | Meaning |
|---|---|---|
| Absolute path | `/Users/anshgandhi/digital-detactive-8009/README.md` | Starts from the very top (`/`) and works from anywhere |
| Relative path | `mission-00-setup/README.md` | Starts from the folder I'm in now |
| Home shortcut | `~` | Same as `/Users/anshgandhi` |
| Parent | `..` | The folder one level up |

### Permissions

```text
$ ls -l README.md
-rw-r--r--  1 anshgandhi  staff  947 Nov 25 00:59 README.md

$ ls -l /etc/hosts
-rw-r--r--  1 root  wheel  213 Nov  6 10:52 /etc/hosts
```

How to read `-rw-r--r--`:

| Part | Who | Meaning |
|---|---|---|
| `-` | — | It's a file (`d` would mean a directory) |
| `rw-` | Owner | Can read and write |
| `r--` | Group | Can only read |
| `r--` | Everyone else | Can only read |

My `README.md` is owned by **me**, so I can edit it. `/etc/hosts` is owned by **root** (the system administrator), so I can read it but can't change it without `sudo`.

**Experiment:** I made a test copy, took away my own write permission, and tried to write to it:

```text
$ chmod 400 perm-test.txt
$ ls -l perm-test.txt
-r--------  1 anshgandhi  staff  59 Nov 25 01:01 perm-test.txt
$ echo x >> perm-test.txt
zsh: permission denied: perm-test.txt
$ chmod 644 perm-test.txt     # put it back
```

Even though I own the file, the OS refused once the permission was gone. Then I deleted the test file.

### Storage

```text
$ df -h /
Filesystem       Size   Used  Avail Capacity  Mounted on
/dev/disk3s1s1  926Gi   13Gi  719Gi     2%    /
```

## Task 3.4 — What the OS is responsible for

| Job | What it means | Where I saw it |
|---|---|---|
| Process management | Decides which program gets the CPU and when | 920 processes sharing 15 cores in `top` |
| Memory management | Gives each app its own RAM and squeezes it when RAM runs low | `PhysMem` and "compressor" in `top` |
| File system | Organises files into folders and tracks where they sit on the SSD | Paths and `df -h` |
| Security and permissions | Controls who can read or change what | `permission denied` in my experiment |
| Device management | Talks to the keyboard, screen, Wi-Fi, speakers through drivers | System Settings → hardware just works |
| User interface | Gives me a way to use the computer | Finder, the Dock, and the Terminal |

## Commands used

`sw_vers`, `uname -sr`, `uname -m`, `whoami`, `ps aux`, `ps -o pid,ppid,comm`, `top -l 1`, `df -h`, `ls -l`, `chmod`, `echo $HOME`, Activity Monitor

## What I understood

The operating system is a manager that sits between my apps and the hardware. Apps never talk to the CPU, RAM or SSD directly. They ask macOS, and macOS decides. That's how 920 processes can share one chip without crashing into each other.

The permissions experiment made it clear. I owned the file, but once the write permission was off, macOS blocked me anyway. That's the same protection that stops a random app from editing system files like `/etc/hosts`.

I also didn't know "macOS" and "Darwin" were different names. Darwin is the kernel underneath, and macOS is the full system built on top of it.

## Problems I ran into

- **Problem:** The `ps aux` output was so long I couldn't read it.
  **Fix:** I piped it into `wc -l` to count the lines, and into `head` to see just the top ones (a trick from Mission 02).
- **Problem:** I didn't understand the letters in `-rw-r--r--`.
  **Fix:** I split it into three groups of three (owner / group / others) and the `chmod 400` experiment showed what removing `w` actually does.

## Evidence

- [`../evidence/mission-03-os-info.txt`](../evidence/mission-03-os-info.txt), the raw output of the commands above
