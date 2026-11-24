# Mission 04 — How Programs Run

## Goal

Write and run a Python program, then find out how that's different from a compiled language by building the same kind of program in C.

## Task 4.1 — My Python program

[`hello.py`](hello.py):

```python
# Mission 04 - my first Python program
name = "Ansh"
print(f"Hi, I'm {name} and this is my Digital Detective project.")

year = 2026
print(f"{year} in binary is {bin(year)[2:]}")
```

Running it:

```text
$ cd mission-04-programs
$ python3 hello.py
Hi, I'm Ansh and this is my Digital Detective project.
2026 in binary is 11111101010
```

What happens when I type `python3 hello.py`:
1. The shell finds the `python3` program (Python 3.14.6 on my Mac).
2. Python reads `hello.py` from the SSD.
3. Python turns my code into **bytecode** and runs it line by line in the Python interpreter.
4. `print()` sends the text to the Terminal (output).

The second line is a preview of Mission 05: `bin()` turns a number into binary.

## Task 4.2 — Compiler vs interpreter

To see the difference myself, I also wrote a tiny C program, [`hello.c`](hello.c), and compiled it with Apple's `clang` compiler:

```text
$ clang --version
Apple clang version 21.0.0

$ clang hello.c -o hello     # step 1: compile (translate the whole file)
$ ./hello                    # step 2: run the finished program
Hi from C, compiled first!

$ file hello
hello: Mach-O 64-bit executable arm64
```

The compiler turned my 96-byte text file into a 33 KB **machine-code** file built for my arm64 chip. After that I can run `./hello` without the compiler at all.

Then I tested how Python handles a mistake, using a file whose second line is broken:

```text
$ python3 t.py
line 1 runs
NameError: name 'oops' is not defined
```

Line 1 still ran before Python reached the error on line 2. A C compiler would refuse to build the program at all and nothing would run.

| | Compiler (C with `clang`) | Interpreter (Python) |
|---|---|---|
| When translation happens | All at once, before running | Line by line, while running |
| What you get | A separate executable file (`hello`) | No separate file; you need `python3` every time |
| Speed | Usually faster to run | Usually slower, but quicker to try changes |
| Errors | Found before the program runs | Found when that line is reached |
| Portability | The executable only works on the chip it was built for (arm64) | The same `.py` file runs anywhere Python is installed |
| Examples | C, C++, Rust, Go | Python, JavaScript, Ruby |

## Commands used

`python3 hello.py`, `python3 --version`, `clang hello.c -o hello`, `./hello`, `file`, `ls -l`

## What I understood

A computer only understands machine code, the 1s and 0s for its own chip. Everything I write has to be translated. A **compiler** translates the whole program once and gives me a finished file. An **interpreter** translates as it goes, every time I run it.

Running both versions made this clear. After `clang` finished, the `hello` file was a real arm64 program that runs on its own. With Python there's no file like that; `python3` has to be there every time.

Python is good for learning and experimenting because I can change a line and run it again straight away. C is better when speed matters, like games or operating systems. (A lot of Python itself is written in C.)

## Problems I ran into

- **Problem:** `./hello` said "no such file or directory" when I ran it in the wrong folder.
  **Fix:** `pwd` showed I wasn't in `mission-04-programs`. After `cd` into it, it worked.
- **Problem:** I wasn't sure if the compiled `hello` file should go on GitHub.
  **Fix:** I left it out using `.gitignore`. It's built from `hello.c` and only works on arm64 Macs, so the source is what matters.

## Evidence

- [`hello.py`](hello.py), my Python program
- [`hello.c`](hello.c), the C program used for the comparison
- Terminal output is copied into the code blocks above
