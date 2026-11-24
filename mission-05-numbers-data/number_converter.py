"""Mission 05 - number converter.

Converts a number between decimal, binary and hexadecimal.
Usage:
    python3 number_converter.py           (asks for input)
    python3 number_converter.py 25        (decimal)
    python3 number_converter.py 0b11001   (binary)
    python3 number_converter.py 0x19      (hex)
"""
import sys


def to_binary(n):
    """Repeated division by 2, done by hand instead of using bin()."""
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n = n // 2
    return bits


def parse(text):
    """Work out which base the input is in from its prefix."""
    text = text.strip().lower()
    if text.startswith("0b"):
        return int(text[2:], 2)
    if text.startswith("0x"):
        return int(text[2:], 16)
    return int(text)


def convert(text):
    n = parse(text)
    if n < 0:
        raise ValueError("please use a number that is 0 or more")
    return {
        "decimal": str(n),
        "binary": to_binary(n),
        "hexadecimal": format(n, "X"),
    }


def main():
    text = sys.argv[1] if len(sys.argv) > 1 else input("Number (e.g. 25, 0b1010, 0x1F): ")
    try:
        result = convert(text)
    except ValueError as err:
        print(f"Sorry, that didn't work: {err}")
        return
    for base, value in result.items():
        print(f"{base:>12}: {value}")


if __name__ == "__main__":
    main()
