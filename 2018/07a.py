#!/usr/bin/env python3
import pytest
import re
from collections import defaultdict
from itertools import chain
DAY='07'


def answer(in_lines):
  #print('\n'.join(in_lines))
  blockers = defaultdict(list)
  for in_line in in_lines:
    #print('['+in_line.strip()+']')
    m = re.match(r'Step (.) must be finished before step (.) can begin.', in_line.strip())
    if not m:
      continue
    first = m.group(1)
    second = m.group(2)
    blockers[second].append(first)
  #get start node
  print(blockers.keys())
  print(set(chain.from_iterable(blockers.values())))
  start_node = set(chain.from_iterable(blockers.values())) - set(blockers.keys())
  print(start_node)
  completed = sorted(list(start_node))
  while True:
    available = []
    for cur_char in blockers.keys():
      if cur_char in completed:
        continue
      if all(av in completed for av in blockers[cur_char]):
        available.append(cur_char)

    if not available:
      break
    available.sort()
    print(''.join(available))
    completed.append(available[0])
    print(completed)
  return ''.join(completed)

@pytest.fixture
def example_input():
  return '''
  Step C must be finished before step A can begin.
  Step C must be finished before step F can begin.
  Step A must be finished before step B can begin.
  Step A must be finished before step D can begin.
  Step B must be finished before step E can begin.
  Step D must be finished before step E can begin.
  Step F must be finished before step E can begin.
  '''

def test_answer(example_input):
  assert answer(sorted(example_input.split('\n'))) == 'CABDFE'

if __name__ == '__main__':
  with open('{}.input'.format(DAY), 'r') as in_file:
    print(answer(sorted(in_file.readlines())))


