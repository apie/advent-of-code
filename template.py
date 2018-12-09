#!/usr/bin/env python3
import pytest

def answer(in_lines):
  pass

@pytest.fixture
def example_input():
  return '''
  '''

def test_answer(example_input):
  assert answer(example_input.split('\n')) == 1

if __name__ == '__main__':
  with open('XX.input', 'r') as in_file:
    print(answer(in_file.readlines()))


