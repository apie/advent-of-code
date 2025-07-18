#!/usr/bin/env python3
from collections import deque


def supportsTLS(ip: str):
    # print(ip)
    stack = deque([], 4)
    foundAbba = False
    inbrack = False
    foundAbbaInbrack = False
    for c in ip:
        if c == "[" or c == "]":
            inbrack = not inbrack
            stack.clear()
            continue
        stack.append(c)
        if len(stack) == 4:
            if stack[0] == stack[3] and stack[1] == stack[2] and stack[0] != stack[1]:
                if inbrack:
                    foundAbbaInbrack = True
                else:
                    foundAbba = True
            continue

    # print(f"{foundAbba=}")
    # print(f"{foundAbbaInbrack=}")
    supports = foundAbba and not foundAbbaInbrack
    # print(ip, 'supports TLS:', supports)
    # print()
    return supports


samples = [
    ("abba[mnop]qrst", True),  # supports TLS (abba outside square brackets).
    (
        "abcd[bddb]xyyx",
        False,
    ),  # does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
    (
        "aaaa[qwer]tyui",
        False,
    ),  # does not support TLS (aaaa is invalid; the interior characters must be different).
    (
        "ioxxoj[asdfgh]zxcvbn",
        True,
    ),  # supports TLS (oxxo is outside square brackets, even though it's within a larger string).
]


def numsupportTLS(ips):
    return sum(supportsTLS(ip) for ip in ips)


for sample, expected in samples:
    assert supportsTLS(sample) == expected, sample
assert numsupportTLS([s[0] for s in samples]) == 2

with open("d07.input", "r") as f:
    lines = f.readlines()
    inp_lines = [line.strip() for line in lines]
# print(lines)
answer = numsupportTLS(inp_lines)
print("Part1:", answer)
