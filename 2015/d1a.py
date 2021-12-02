#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def answer(lines):
    f = 0
    for line in map(str.strip, lines):
        for c in line:
            if c == '(':
                f += 1
            if c == ')':
                f -= 1
    return f

@pytest.mark.parametrize( "inp,outp", [
    ('(())', 0),
    ('()()', 0),
    ('(((', 3),
    ('(()(()(', 3),
    ('))(((((', 3),
    ('())', -1),
    ('))(', -1),
    (')))', -3),
    (')())())', -3),
])
def test_answer(inp, outp):
    assert answer(inp) == outp

if __name__ == '__main__':
    print(answer(fileinput.input(F_NAME + '.input')))

