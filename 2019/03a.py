#!/usr/bin/env python3
from dataclasses import dataclass
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]


@dataclass
class Coordinate:
    x: int
    y: int


def answer(lines):
    c1 = dict(c=Coordinate(x=0, y=0), visited=set())
    c2 = dict(c=Coordinate(x=0, y=0), visited=set())
    cs = iter((c1, c2))
    crosses = []
    for line in map(str.strip, lines):
        cc = next(cs)
        for instr in line.split(','):
            direction, t_amount = instr[0], instr[1:]
            t_amount = int(t_amount)
            for _ in range(t_amount):
                if direction == 'U':
                    cc['c'].y += 1
                elif direction == 'D':
                    cc['c'].y -= 1
                elif direction == 'L':
                    cc['c'].x -= 1
                elif direction == 'R':
                    cc['c'].x += 1
                else:
                    raise Exception()
                coord = (cc['c'].x, cc['c'].y)
                if not c2['visited']:
                    cc['visited'].add(coord)
                if c2['visited'] and coord in c1['visited']:
                    crosses.append(coord)
    print(f'{crosses=}')
    sum_nearest_cross = min(
        abs(cr[0]) + abs(cr[1])
        for cr in crosses
    )
    return sum_nearest_cross


@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')


def test_answer(example_input):
    assert answer(example_input) == 6


@pytest.fixture
def example_input2():
    return fileinput.input(F_NAME + '.test2')


def test_answer2(example_input2):
    assert answer(example_input2) == 159


@pytest.fixture
def example_input3():
    return fileinput.input(F_NAME + '.test3')


def test_answer3(example_input3):
    assert answer(example_input3) == 135


if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')
