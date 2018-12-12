#!/usr/bin/env python3
import pytest
DAY=12

def get_sum(i):
  assert i >= 7447
  return 485011 + (i-7447)*65

def test_get_sum():
  assert get_sum(7447) == 485011
  assert get_sum(7447+5) == get_sum(7447) + 65*5

if __name__ == '__main__':
  """
  Found out the following while running the loop and printing the i and diff with last sum:
  i: 7447
  Sum: 485011
  Diff: 65

  so the increase is 65 with each iteration
  """
  print('Answer: {}'.format(get_sum(50000000000)))


