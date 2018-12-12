#!/usr/bin/env python3
import pytest
import string

def reduce_str(in_str):
  finished = False
  tmp_str = in_str
  sub_result = tmp_str
  i = 0
  while not finished:
    i += 1
    print(i)
    for char in string.ascii_lowercase:
      sub_result = sub_result.replace(char.lower()+char.upper(), '').replace(char.upper()+char.lower(), '')
    if sub_result == tmp_str:
      finished = True
    tmp_str = sub_result
  return tmp_str
    


@pytest.fixture
def example_input():
  return 'dabAcCaCBAcCcaDA'

def test_reduce_str(example_input):
  reduced = reduce_str(example_input)
  assert reduced == 'dabCBAcaDA'
  assert len(reduced) == 10


if __name__ == '__main__':
  with open('05.input', 'r') as in_list:
    print(len(reduce_str(in_list.readline().strip())))


