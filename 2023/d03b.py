#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath

F_NAME = splitext(abspath(__file__))[0][:-1]


def findnumber(engine, x, y):
    number = ""
    # gegeven xy coordinaat. zoek het volledige nummer dat daar ligt
    c = engine[y][x]
    if not c.isnumeric():
        return 0
    # schuif eerst naar links (begin van nr)
    while c.isnumeric():
        x -= 1
        c = engine[y][x]
    x += 1
    c = engine[y][x]
    # loop over nummer
    while c.isnumeric():
        number += c
        x += 1
        try:
            c = engine[y][x]
        except IndexError:
            c = "."
    return int(number) if number else 0


def answer(lines):
    answer = 0
    print()
    engine = []
    for line in map(str.strip, lines):
        engine.append(line)

    ll = len(line)
    el = len(engine)
    for y in range(el):
        for x in range(ll):
            c = engine[y][x]
            if c != "*":
                continue
            print("Gear position:", y, ",", x)
            numbers = set()
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    if n := findnumber(engine, x + dx, y + dy):
                        # print('found number!! ', n)
                        numbers.add(n)
            if len(numbers) == 2:
                print("Partnumbers:", numbers)
                answer += numbers.pop() * numbers.pop()
            numbers.clear()

    print(answer)
    return answer


def test_findnumber():
    assert findnumber(["123...#456..."], 1, 0) == 123
    assert findnumber(["123...#456..."], 2, 0) == 123
    assert findnumber(["123...#456..."], 4, 0) == 0
    assert findnumber(["123...#456..."], 7, 0) == 456


@pytest.mark.parametrize(
    "testfileno, expected",
    [
        (1, 467835),
    ],
)
def test_answer_testfiles(testfileno, expected):
    assert answer(fileinput.input(f"{F_NAME}.test.{testfileno}")) == expected


if __name__ == "__main__":
    import timeit

    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + ".input")
    ans = answer(filename)
    assert ans > 20125432
    print("Answer:", ans)
    duration = timeit.default_timer() - start
    print(f"Execution time: {duration:.3f} s")
