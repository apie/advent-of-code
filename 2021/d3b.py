#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def get_oxygen_generator_rating(lines):
    lines = list(map(str.strip, lines))
    nlines = len(lines)
    print(lines)
    line_length = len(lines[0])
    reducedlines = [l for l in lines]
    for c in range(line_length):
        onescount = 0
        for l in range(len(reducedlines)):
            line = reducedlines[l]
            col = line[c]
            onescount += int(col)
        zeroscount = len(reducedlines) - onescount
        mostcommonbit = 1 if onescount >= zeroscount else 0
        print(f'{c=} {onescount=} {zeroscount=} {mostcommonbit=}')
        reducedlines = [l for l in reducedlines if l[c] == str(mostcommonbit)]
        print(len(reducedlines), reducedlines)
    oxygen_generator_rating = reducedlines[0]
    print(oxygen_generator_rating)
    return int(oxygen_generator_rating, 2)

def get_co2_scrubber_rating(lines):
    lines = list(map(str.strip, lines))
    nlines = len(lines)
    print(lines)
    line_length = len(lines[0])
    reducedlines = [l for l in lines]
    for c in range(line_length):
        onescount = 0
        for l in range(len(reducedlines)):
            line = reducedlines[l]
            col = line[c]
            onescount += int(col)
        zeroscount = len(reducedlines) - onescount
        mostcommonbit = 0 if onescount >= zeroscount else 1
        print(f'{c=} {onescount=} {zeroscount=} {mostcommonbit=}')
        reducedlines = [l for l in reducedlines if l[c] == str(mostcommonbit)]
        print(len(reducedlines), reducedlines)
        if len(reducedlines) == 1:
            break
    co2_scrubber_rating = reducedlines[0]
    print(co2_scrubber_rating)
    return int(co2_scrubber_rating, 2)


def answer(lines):
    lines = list(lines)
    return get_oxygen_generator_rating(lines)*get_co2_scrubber_rating(lines) # life support rating


@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + 'a.test')

def test_oxygen(example_input):
    assert get_oxygen_generator_rating(example_input) == 23
def test_co2(example_input):
    assert get_co2_scrubber_rating(example_input) == 10
def test_answer(example_input):
    assert answer(example_input) == 230

if __name__ == '__main__':
    print(answer(fileinput.input(F_NAME + '.input')))

