#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath


def answer(in_lines):
    pass

@pytest.fixture
def example_input():
    return '''
    '''

def test_answer(example_input):
    assert answer(iter(example_input.split('\n'))) == 1

if __name__ == '__main__':
    print(answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input')))

