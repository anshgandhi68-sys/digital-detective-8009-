# Mission 05 — Numbers and Data

## Goal

Convert between decimal, binary and hexadecimal by hand, check the answers with Python, build my own converter, and find out how text is stored as numbers.

## Quick reference

| Base | Name | Digits used | Python prefix |
|---|---|---|---|
| 10 | Decimal | 0–9 | (none) |
| 2 | Binary | 0, 1 | `0b` |
| 16 | Hexadecimal | 0–9 and A–F (A=10 … F=15) | `0x` |

Binary place values: `128 64 32 16 8 4 2 1`

## Task 5.1 — Conversions by hand

### A. 13 (decimal) → binary

Divide by 2 and keep the remainders, then read them **bottom to top**:

| Divide | Result | Remainder |
|---|---|---|
| 13 ÷ 2 | 6 | **1** |
| 6 ÷ 2 | 3 | **0** |
| 3 ÷ 2 | 1 | **1** |
| 1 ÷ 2 | 0 | **1** |

**13 = 1101₂**. Check: 8 + 4 + 0 + 1 = 13 ✔

### B. 25 (decimal) → binary

| Divide | Result | Remainder |
|---|---|---|
| 25 ÷ 2 | 12 | **1** |
| 12 ÷ 2 | 6 | **0** |
| 6 ÷ 2 | 3 | **0** |
| 3 ÷ 2 | 1 | **1** |
| 1 ÷ 2 | 0 | **1** |

**25 = 11001₂**. Check: 16 + 8 + 0 + 0 + 1 = 25 ✔

### C. 1010₂ → decimal

| Bit | 1 | 0 | 1 | 0 |
|---|---|---|---|---|
| Place value | 8 | 4 | 2 | 1 |
| Bit × value | 8 | 0 | 2 | 0 |

8 + 2 = **10**

### D. 1101₂ → decimal

| Bit | 1 | 1 | 0 | 1 |
|---|---|---|---|---|
| Place value | 8 | 4 | 2 | 1 |
| Bit × value | 8 | 4 | 0 | 1 |

8 + 4 + 1 = **13**. Same as A, which shows the conversion works in both directions.

### E. A₁₆ → decimal

In hex, A stands for **10**. So A₁₆ = **10**.

### F. 1F₁₆ → decimal

Hex place values are `16 1`.
(1 × 16) + (F × 1) = 16 + 15 = **31**

### G. 1111₂ → hexadecimal

One hex digit = exactly four binary bits. 1111₂ = 8 + 4 + 2 + 1 = 15, and 15 in hex is **F**.

## Task 5.2 — Checking with Python

```text
$ python3
>>> bin(13), bin(25)
('0b1101', '0b11001')
>>> int('1010', 2), int('1101', 2)
(10, 13)
>>> int('A', 16), int('1F', 16)
(10, 31)
>>> hex(0b1111)
'0xf'
```

All seven answers match my working above. ✔

## Task 5.3 — My number converter

[`number_converter.py`](number_converter.py) takes a number in **any** of the three bases and shows it in all three. It works out the base from the prefix (`0b` for binary, `0x` for hex).

I wrote my own `to_binary()` function that does the repeated division from Task 5.1, instead of just calling `bin()`, so the program uses the same method I did by hand.

### Functions

| Function | Job |
|---|---|
| `to_binary(n)` | Repeated ÷ 2, building the remainders into a string |
| `parse(text)` | Reads the input and works out if it's decimal, binary or hex |
| `convert(text)` | Returns the number in all three bases; rejects negatives |
| `main()` | Takes the number from the command line, or asks for it |

### Test runs

```text
$ python3 number_converter.py 25
     decimal: 25
      binary: 11001
 hexadecimal: 19

$ python3 number_converter.py 0x1F
     decimal: 31
      binary: 11111
 hexadecimal: 1F

$ python3 number_converter.py 0b1111
     decimal: 15
      binary: 1111
 hexadecimal: F
```

| Input | Expected | Got | Pass? |
|---|---|---|---|
| `13` | 1101 / D | 1101 / D | ✔ |
| `25` | 11001 / 19 | 11001 / 19 | ✔ |
| `0b1010` | 10 / A | 10 / A | ✔ |
| `0b1101` | 13 / D | 13 / D | ✔ |
| `0xA` | 10 / 1010 | 10 / 1010 | ✔ |
| `0x1F` | 31 / 11111 | 31 / 11111 | ✔ |
| `0` | 0 / 0 / 0 | 0 / 0 / 0 | ✔ |
| `-5` | error message | "please use a number that is 0 or more" | ✔ |
| `abc` | error message, no crash | "Sorry, that didn't work: …" | ✔ |

## Task 5.4 — How text is stored

Computers can only store numbers, so every character is given a number code.

```text
>>> ord('A'), ord('a'), ord('0'), ord(' ')
(65, 97, 48, 32)
```

| Character | ASCII code | Binary |
|---|---|---|
| `A` | 65 | 01000001 |
| `a` | 97 | 01100001 |
| `0` | 48 | 00110000 |
| space | 32 | 00100000 |

Interesting things I found:
- Capital and small letters are exactly **32 apart** (`A`=65, `a`=97), so changing case is just flipping one bit.
- The *character* `'0'` is 48, not 0. Text digits and real numbers are stored differently.

**Why do we need an encoding standard?** If my Mac stored `A` as 65 but another computer read 65 as something else, every message would come out scrambled. A shared standard like ASCII or UTF-8 means everyone agrees on which number means which character.

**A character outside basic ASCII:** ASCII only has 128 characters, which is enough for English but not much else. The Indian rupee sign `₹` is code **8377** in Unicode, and UTF-8 stores it in 3 bytes:

```text
>>> ord('₹')
8377
>>> '₹'.encode('utf-8')
b'\xe2\x82\xb9'
```

That's why the web uses **UTF-8**: it covers every language (and emoji) but still stores plain English in 1 byte per letter, the same as ASCII.

## Commands used

`python3`, `bin()`, `hex()`, `int(x, base)`, `ord()`, `str.encode('utf-8')`, `python3 number_converter.py`

## What I understood

Decimal, binary and hex are just different ways of writing the same number. 25, 11001₂ and 19₁₆ all mean the same amount. Computers use binary because a circuit is either on or off. Programmers use hex because it's a short way to write binary: every 4 bits become one hex digit.

Doing the conversions by hand first, and then writing `to_binary()` with the same "divide by 2, keep the remainder" method, helped me actually understand it instead of just trusting `bin()`.

The text part connected everything. A letter on my screen is really a number like 65, stored as 01000001. Encodings like UTF-8 are agreements that make sure every computer reads those numbers the same way.

## Problems I ran into

- **Problem:** My first binary answers came out backwards (I got 1011 for 13).
  **Fix:** The remainders have to be read from the **bottom up**. Checking with place values (8+4+1) caught it.
- **Problem:** The converter crashed with a long error when I typed a word.
  **Fix:** I wrapped the conversion in `try/except ValueError`, so it now prints a friendly message instead.

## Evidence

- [`number_converter.py`](number_converter.py), my converter
- Test runs and Python checks are copied into the code blocks above
