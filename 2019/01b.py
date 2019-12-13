#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath


def calc(x):
    ans = (x//3)-2 
    return ans+calc(ans) if ans > 0 else 0

def answer(in_lines):
    return sum(
        calc(int(l)) for l in in_lines
        if l.strip() != ''
    )

@pytest.fixture
def example_input():
    return '''
    1969
    '''

def test_answer(example_input):
    assert answer(iter(example_input.split('\n'))) == 966

if __name__ == '__main__':
    print(answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input')))

