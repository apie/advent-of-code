#!/usr/bin/env python3
import pytest
DAY=0

def answer(in_lines):
  pass

@pytest.fixture
def example_input():
  return '''
  '''

def test_answer(example_input):
  assert answer(example_input.split('\n')) == 1

if __name__ == '__main__':
  with open('{:02}.input'.format(DAY), 'r') as in_file:
    print(answer(in_file.readlines()))


