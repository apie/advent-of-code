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
        perimeters = []
        perimeters.append(l+w)
        perimeters.append(w+h)
        perimeters.append(h+l)
        smallest_perimeter=min(perimeters)
        wrap = 2*smallest_perimeter
        bow = l*w*h
        tot += wrap + bow
    return tot

@pytest.mark.parametrize( "inp,outp", [
    (['2x3x4'], 34),
    (['1x1x10'], 14),
])
def test_answer(inp, outp):
    assert answer(inp) == outp

if __name__ == '__main__':
    print(answer(fileinput.input(F_NAME + '.input')))

