#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath

'''
To do this, count the number of times a depth measurement increases from the previous measurement.
'''

def answer(in_lines):
    times_increased = 0
    prev = None
    for line in in_lines:
        line = line.strip()
        if not line:
            continue
#        print(line)
        num = int(line)
        if prev and num > prev:
            times_increased += 1
        prev = num
    return times_increased


@pytest.fixture
def example_input():
    return '''
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    '''

def test_answer(example_input):
    assert answer(iter(example_input.split('\n'))) == 7

if __name__ == '__main__':
    print(answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input')))

