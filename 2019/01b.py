#!/usr/bin/env python3
import pytest
DAY='01'

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
    assert answer(example_input.split('\n')) == 966


if __name__ == '__main__':
  with open('{}.input'.format(DAY), 'r') as in_file:
    print(answer(in_file.readlines()))


