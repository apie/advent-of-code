#!/usr/bin/env python3
import pytest
DAY='{{cookiecutter.day|replace('a','')|replace('b', '')}}'

def answer(in_lines):
  pass

@pytest.fixture
def example_input():
  return '''
  '''

def test_answer(example_input):
  assert answer(example_input.split('\n')) == 1

if __name__ == '__main__':
  with open('{}.input'.format(DAY), 'r') as in_file:
    print(answer(in_file.readlines()))


