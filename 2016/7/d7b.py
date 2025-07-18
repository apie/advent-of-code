#!/usr/bin/env python3
from collections import deque


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    @staticmethod
    def ok(s: str) -> str:
        return f"{bcolors.OKGREEN}{s}{bcolors.ENDC}"

    @staticmethod
    def warning(s: str) -> str:
        return f"{bcolors.WARNING}{s}{bcolors.ENDC}"

    @staticmethod
    def fail(s: str) -> str:
        return f"{bcolors.FAIL}{s}{bcolors.ENDC}"


samples = [
    # supports SSL (aba outside square brackets with corresponding bab within square brackets).
    ("aba[bab]xyz", True),
    # does not support SSL (xyx, but no corresponding yxy).
    ("xyx[xyx]xyx", False),
    # supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
    ("aaa[kek]eke", True),
    # supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
    ("zazbz[bzb]cdb", True),
]


def supportsSSL(ip: str):
    abas = set()
    babs = set()
    stack = deque([], 3)
    inbrack = False
    for c in ip:
        if c == "[" or c == "]":
            inbrack = not inbrack
            stack.clear()
            continue
        stack.append(c)
        if len(stack) == 3:
            if stack[0] == stack[2] and stack[0] != stack[1]:
                if inbrack:
                    # print('found bab')
                    babs.add("".join(stack))
                else:
                    # print('found aba')
                    abas.add("".join(stack))

    # print(f"{abas=}")
    # print(f"{babs=}")
    def getbab(aba: str) -> str:
        return aba[1] + aba[0] + aba[1]

    found = False
    for aba in abas:
        if getbab(aba) in babs:
            found = True
            break
    print(ip, "supports SSL:", bcolors.ok(found) if found else bcolors.fail(found))
    # print()
    return found


def numsupportSSL(ips):
    return sum(supportsSSL(ip) for ip in ips)


for sample, expected in samples:
    assert supportsSSL(sample) == expected, sample
assert numsupportSSL([s[0] for s in samples]) == 3
# assert False

with open("d07.input", "r") as f:
    lines = f.readlines()
    inp_lines = [line.strip() for line in lines]
answer = numsupportSSL(inp_lines)
print("Part2:", bcolors.warning(answer))
