#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def answer(lines):
    lines = list(lines)
    gammarate = get_gammarate(lines)
    return gammarate*get_epsilonrate(gammarate, lines) #power consumption

def get_gammarate(lines):
    lines = list(map(str.strip, lines))
    nlines = len(lines)
    ilines = iter(lines)
    line_length = len(lines[0])
    print(line_length)
    gammarate = ''
    for col in range(line_length):
        onescount = 0
        for line in ilines:
            try:
                c = line[col]
            except IndexError:
                continue
#            print(c)
            onescount += int(c)
        zeroscount = nlines - onescount
        mostcommonbit = 1 if onescount > zeroscount else 0
        gammarate += str(mostcommonbit)
        print('-col', col, mostcommonbit)
        ilines = iter(lines)
    gammarate = int(gammarate, 2)
    print(gammarate)
    return gammarate

def get_epsilonrate(gammarate, lines):
    lines = list(map(str.strip, lines))
    line_length = len(lines[0])
    print(line_length)
    epsilonrate = gammarate ^ int('1'*line_length, 2)
    return epsilonrate


@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + 'a.test')

def test_answer(example_input):
    assert answer(example_input) == 198

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)
