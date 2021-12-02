#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]


def answer(lines):
    h = d = a = 0
    for line in map(str.strip, lines):
        instruction, amount = line.split()
        amount = int(amount)
        if instruction == 'forward':
            h += amount
            d += a*amount
        elif instruction == 'down':
            a += amount
        elif instruction == 'up':
            a -= amount
    print(h, d)
    return h*d

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 900

if __name__ == '__main__':
    print(answer(fileinput.input(F_NAME + '.input')))

