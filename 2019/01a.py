#!/usr/bin/env python3
import pytest
DAY='01'

def answer(in_lines):
  return sum((int(l)//3)-2 for l in in_lines if l.strip() != '')

@pytest.fixture
def example_input():
  return '''
  12
  '''
  #14
  #1969
  #100756

def test_answer(example_input):
    assert answer(example_input.split('\n')) == 2 #2, 654, 33583


if __name__ == '__main__':
  with open('{}.input'.format(DAY), 'r') as in_file:
    print(answer(in_file.readlines()))


