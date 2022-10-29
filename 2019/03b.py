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
    c1 = dict(name=1, c=Coordinate(x=0, y=0),
              visited_set=set(), visited=list())
    c2 = dict(name=2, c=Coordinate(x=0, y=0), visited=0)
    cs = iter((c1, c2))
    min_cross = 999999999999999
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
                if cc['name'] == 1:
                    cc['visited_set'].add(coord)
                    cc['visited'].append(coord)
                else:
                    cc['visited'] += 1
                if c2['visited'] and coord in c1['visited_set']:
                    cross_steps = c1['visited'].index(
                        coord) + 1 + cc['visited']
                    if cross_steps < min_cross:
                        min_cross = cross_steps
    return min_cross


@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')


def test_answer(example_input):
    assert answer(example_input) == 30


@pytest.fixture
def example_input2():
    return fileinput.input(F_NAME + '.test2')


def test_answer2(example_input2):
    assert answer(example_input2) == 610


@pytest.fixture
def example_input3():
    return fileinput.input(F_NAME + '.test3')


def test_answer3(example_input3):
    assert answer(example_input3) == 410


if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')
