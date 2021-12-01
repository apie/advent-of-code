#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
from d1a import answer as answer_1a

'''
To do this, count the number of times a depth measurement increases from the previous measurement.
Instead, consider sums of a three-measurement sliding window.
'''

def answer(in_lines):
    windows = []
    prev = []
    for line in in_lines:
        line = line.strip()
        if not line:
            continue
        num = int(line)
        prev.append(num)
        if len(prev) >= 3:
            # append sum of last 3 items
            windows.append(sum(d for d in prev[-3:]))
    return answer_1a(map(str, windows))


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
    assert answer(iter(example_input.split('\n'))) == 5

if __name__ == '__main__':
    print(answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input')))

