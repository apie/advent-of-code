#!/usr/bin/env python3
#10,68 seconds if using the original string as input
# 1,30 seconds if using the reduced string as input
import pytest
import string
from operator import itemgetter

def reduce_str(in_str):
  finished = False
  tmp_str = in_str
  sub_result = tmp_str
  while not finished:
    for char in string.ascii_lowercase:
      sub_result = sub_result.replace(char.lower()+char.upper(), '').replace(char.upper()+char.lower(), '')
    if sub_result == tmp_str:
      finished = True
    tmp_str = sub_result
  return tmp_str

def find_smallest(in_line):
  results = []
  for char in string.ascii_lowercase:
    results.append((char, len(reduce_str(in_line.replace(char, '').replace(char.upper(), '')))))
  return sorted(results, key=itemgetter(1))[0]



@pytest.fixture
def example_input():
  return 'dabAcCaCBAcCcaDA'

def test_reduce_str(example_input):
  reduced = reduce_str(example_input)
  assert reduced == 'dabCBAcaDA'
  assert len(reduced) == 10

def test_find_smallest(example_input):
  assert find_smallest(example_input) == ('c', 4)

if __name__ == '__main__':
  with open('05.input', 'r') as in_list:
    print(find_smallest(reduce_str(in_list.readline().strip())))


