#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
from dataclasses import dataclass
from itertools import cycle


@dataclass
class Coordinate:
    x: int
    y: int


def answer(lines):
    line = next(map(str.strip, lines))
    lines.close()
#    print(line)
    santa = Coordinate(x=0, y=0)
    robo_santa = Coordinate(x=0, y=0)
    visitors = cycle((santa, robo_santa))
    visitor = next(visitors)
    houses_visited = {str(visitor)}
    for c in line:
        if c == '>':
            visitor.x += 1
        elif c == '<':
            visitor.x -= 1
        elif c == '^':
            visitor.y += 1
        elif c == 'v':
            visitor.y -= 1
        else:
            raise Exception('Unknown character')
        houses_visited.add(str(visitor))
        visitor = next(visitors)
#        print(houses_visited)
    return len(houses_visited)

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test.4')

def test_answer(example_input):
    assert answer(example_input) == 3

@pytest.fixture
def example_input2():
    return fileinput.input(F_NAME + '.test.2')

def test_answer2(example_input2):
    assert answer(example_input2) == 3

@pytest.fixture
def example_input3():
    return fileinput.input(F_NAME + '.test.3')

def test_answer3(example_input3):
    assert answer(example_input3) == 11

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

