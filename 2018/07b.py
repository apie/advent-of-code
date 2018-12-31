#!/usr/bin/env python3
import pytest
import re
from collections import defaultdict
from itertools import chain
DAY='07'

def answer(in_lines, num_workers, time_sub):
  blockers = defaultdict(list)
  for in_line in in_lines:
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
  time = -1
  #increase time for start node(s)
  #assume all start chars were executed in parallel
  assert len(completed) <= num_workers
  #take time of highest char
  time += ord(completed[-1])-time_sub-4 # A: 61, B: 62 etc
  workers = []
  while True:
    available = []
    for cur_char in blockers.keys():
      if cur_char in completed:
        continue
      if all(av in completed for av in blockers[cur_char]):
        available.append(cur_char)

    print(time)
    if not available and len(workers) == 0:
      break
    time += 1
    available.sort()
    print(''.join(available))
    # Assign work
    for candidate in available:
      for n in range(num_workers):
        if not any(candidate in w for w in workers):
          if n > len(workers)-1:
            workers.append(dict())
          if len(workers[n]) == 0:
            workers[n][candidate] = ord(candidate)-time_sub-4 # A: 61, B: 62 etc
    print('Waiting ',workers)
    # Do work
    for w in workers:
      assert len(w.keys()) <= 1
      ready = None
      for c in w.keys():
        w[c] -= 1
        if w[c] <= 0:
          ready = c
      if ready:
        workers.remove(w)
        completed.append(ready)
    print(completed)
  return time, ''.join(completed)

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
  assert answer(sorted(example_input.split('\n')), num_workers=2, time_sub=60) == (15, 'CABFDE')

if __name__ == '__main__':
  with open('{}.input'.format(DAY), 'r') as in_file:
    print(answer(sorted(in_file.readlines()), num_workers=5, time_sub=0))


