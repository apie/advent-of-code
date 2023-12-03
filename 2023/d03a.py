#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath

F_NAME = splitext(abspath(__file__))[0][:-1]
import re


def answer(lines):
    answer = 0
    engine = []
    for line in map(str.strip, lines):
        print(line)
        engine.append(line)
    print()

    ll = len(line)
    el = len(engine)
    for y in range(el):
        partnumber = ""
        found = False
        for x in range(ll):
            c = engine[y][x]
            if not c.isnumeric():
                continue
            #            print(c)
            l = r = u = d = lu = ru = ld = rd = "."
            try:
                l = engine[y][x - 1]
                lu = engine[y - 1][x - 1]
                u = engine[y - 1][x]
                ru = engine[y - 1][x + 1]
                r = engine[y][x + 1]
                rd = engine[y + 1][x + 1]
                d = engine[y + 1][x]
                ld = engine[y + 1][x - 1]
            except (KeyError, IndexError):
                pass
            #            print('l lu u ru r rd d ld: ', l,lu,u,ru,r,rd,d,ld)
            if re.match(r"[^0-9]", l):
                partnumber = c
            if re.match(r"[0-9]", l):
                partnumber += c
            if found or any(
                re.match(r"[^0-9\.]", z) for z in (l, lu, u, ru, r, rd, d, ld)
            ):
                found = True
                if re.match(r"[^0-9]", r):
                    print("found part number ", partnumber)
                    answer += int(partnumber)
                    partnumber = ""
                    found = False

    #        break
    #        print()
    print(answer)
    return answer


@pytest.mark.parametrize(
    "testfileno, expected",
    [
        (1, 4361),
    ],
)
def test_answer_testfiles(testfileno, expected):
    assert answer(fileinput.input(f"{F_NAME}.test.{testfileno}")) == expected


if __name__ == "__main__":
    import timeit

    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + ".input")
    ans = answer(filename)
    print("Answer:", ans)
    duration = timeit.default_timer() - start
    print(f"Execution time: {duration:.3f} s")
