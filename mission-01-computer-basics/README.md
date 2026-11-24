# Mission 01 — Computer Basics

## Goal

Understand the IPOS cycle (Input → Processing → Output → Storage), tell hardware apart from software, and spot computer systems in everyday life.

## My computer

Found with **Apple menu → About This Mac** (or `system_profiler SPHardwareDataType` in Terminal).

| Part | My Mac |
|---|---|
| Model | MacBook Pro |
| Chip (CPU) | Apple M5 Pro, 15 cores |
| Memory (RAM) | 24 GB |
| Storage (SSD) | ~1 TB (926 GiB usable) |
| Operating system | macOS 27.2.1 |

## Task 1.1 — IPOS cycle

The activity I traced: **recording a short voice clip in GarageBand and saving it.**

| Stage | What happens? | Which part of the computer does it? |
|---|---|---|
| Input | I press record and speak; my voice goes in as sound waves. | Built-in microphone (and the trackpad for clicking Record) |
| Processing | The sound is turned into digital samples, and GarageBand draws the waveform and applies effects. | CPU (M5 Pro chip) using RAM as working memory |
| Output | I see the waveform on screen and hear the playback. | Display and speakers |
| Storage | When I press ⌘S the project is written to a file so it's still there after a restart. | SSD |

## Task 1.2 — Hardware or software?

Each item sorted as hardware, operating system, application or utility.

| Item | Type | What it's for |
|---|---|---|
| Keyboard | Hardware | Typing letters, numbers and shortcuts |
| Trackpad | Hardware | Moving the pointer, clicking and scrolling |
| Screen | Hardware | Showing everything the computer outputs visually |
| SSD | Hardware | Keeping files and apps permanently, even when powered off |
| Speakers | Hardware | Playing sound |
| macOS | Operating system | Runs the Mac: manages memory, files, apps and devices |
| Safari | Application | Browsing websites |
| Visual Studio Code | Application | Writing and editing code and READMEs |
| GarageBand | Application | Recording and editing music |
| Activity Monitor | Utility | Showing which processes are running and how much CPU/RAM they use |

## Task 1.3 — Computers around me

Three systems I see outside my laptop that are also computers.

| System | What it does | One input | One output |
|---|---|---|---|
| Microwave oven | Heats food for a set time and power level | Keypad (time + power buttons) | Heat, the countdown display, and a beep |
| Lift (elevator) | Moves people between floors | Floor button pressed | Lift moves; floor number lights up |
| Self-checkout at a supermarket | Scans and bills items | Barcode scanner | Price on screen and a printed receipt |

## Tools used

| Tool | Why |
|---|---|
| About This Mac | To find my chip, RAM and storage |
| Terminal (`system_profiler`) | Same info from the command line |
| Visual Studio Code | To write this README |

## What I understood

IPOS is the basic loop every computer follows: it takes something in, works on it, shows the result, and saves it if needed. Once I started looking for it, I could see the same four steps in a microwave and a lift, not just in my laptop. Anything that takes input, processes it with rules and gives output is a computer system, even if it has no screen or keyboard.

The difference between RAM and storage surprised me. My Mac has 24 GB of RAM but about 1 TB of SSD. RAM is very fast but only holds what I'm working on right now and is wiped when the Mac turns off. The SSD is slower but keeps everything permanently. That's why unsaved work disappears if an app crashes: it was only in RAM.

Hardware is the physical part, and software is the instructions. Software comes in layers: macOS sits underneath and controls the hardware, apps like GarageBand sit on top for my own tasks, and utilities like Activity Monitor help look after the system.

## Problems I ran into

- I wasn't sure whether Activity Monitor counts as an application or a utility. I put it under utility because it's for looking after the computer, not for doing my own work.
- "Processing" was the hardest stage to describe because you can't see it happen. Thinking about what changes between input and output (raw sound → a waveform with effects) helped.

## Checklist

- [x] Found my Mac's hardware specs
- [x] IPOS table filled in
- [x] Hardware/software table filled in
- [x] Three everyday computer systems listed
- [x] "What I understood" written
- [x] Spec output saved in [`evidence/mission-01-specs.txt`](../evidence/mission-01-specs.txt)
