#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def answer(lines):
    tot = 0
    for line in map(str.strip, lines):
        print(line)
        l, w, h = map(int, line.split('x'))
        sides = []
        sides.append(l*w)
        sides.append(w*h)
        sides.append(h*l)
        print(sides)
        tot += 2*sum(sides) + min(sides) #add smallest side as slack
    return tot

@pytest.mark.parametrize( "inp,outp", [
    (['2x3x4'], 58),
    (['1x1x10'], 43),
])
def test_answer(inp, outp):
    assert answer(inp) == outp

if __name__ == '__main__':
    print(answer(fileinput.input(F_NAME + '.input')))

