#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]


def answer(lines):
    h = d = 0
    for line in map(str.strip, lines):
        instruction, amount = line.split()
        amount = int(amount)
        if instruction == 'forward':
            h += amount
        elif instruction == 'down':
            d += amount
        elif instruction == 'up':
            d -= amount
    print(h, d)
    return h*d

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 150

if __name__ == '__main__':
    print(answer(fileinput.input(F_NAME + '.input')))

