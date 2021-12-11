#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

SCORING = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
OPENING = ('(','[','{','<')
OPEN_TO_CLOSE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

def answer(lines):
    illegal_chars = []
    for line in map(str.strip, lines):
        stack = []

        for i, c in enumerate(line):
            if c in OPENING:
                stack.append(c)
            else:
                expected = OPEN_TO_CLOSE[stack.pop()]
                if c != expected:
                    print(f'{line} {i} Expected {expected}, but found {c} instead.')
                    illegal_chars.append(c)
                    break
#    print(illegal_chars)
    return sum(SCORING[ic] for ic in illegal_chars)

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    print('')
    assert answer(example_input) == 26397

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)

