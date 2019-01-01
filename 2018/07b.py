#!/usr/bin/env python3
import pytest
import re
from collections import defaultdict
from itertools import chain
DAY='07'

def get_time(candidate, time_sub):
  return ord(candidate)-time_sub-4 # A: 61, B: 62 etc

def answer(in_lines, num_workers, time_sub):
  print()
  print('Second Workers Done')
  blockers = defaultdict(list)
  for in_line in in_lines:
    m = re.match(r'Step (.) must be finished before step (.) can begin.', in_line.strip())
    if not m:
      continue
    first = m.group(1)
    second = m.group(2)
    blockers[second].append(first)
  #get start node
  start_node = set(chain.from_iterable(blockers.values())) - set(blockers.keys())
  start_nodes = sorted(list(start_node))
  complete = []
  time = -1
  #assume start nodes can start immediately
  assert len(start_nodes) <= num_workers
  #fill workers
  workers = [(n, get_time(n, time_sub)) for n in start_nodes]
  #add remaining empty workers
  workers.extend([('.', 0)]*(num_workers-len(start_nodes)))
  while True:
    time += 1
    # Determine availables
    available = []
    for cur_char in blockers.keys():
      if cur_char in complete:
        continue
      if all(av in complete for av in blockers[cur_char]):
        available.append(cur_char)
    available.sort()
    
    # Assign work
    for candidate in available:
      if candidate in complete:
        continue
      if not any(candidate == w for w, c in workers):
        for n, _ in enumerate(workers):
          if workers[n][1] == 0:
            workers[n] = (candidate, get_time(candidate, time_sub))
            break

    print('{time: >6} {worker_str: <7} {complete}'.format(
      time=time,
      worker_str=''.join(c for c,t in workers),
      complete=''.join(complete),
    ))
    if not available and sum(c for w,c in workers) == 0:
      break

    # Do work
    for w, _ in enumerate(workers):
      ready = None
      if workers[w][1] > 0:
        letter, t = workers[w]
        t -= 1
        workers[w] = letter, t
        if workers[w][1] <= 0:
          complete.append(workers[w][0])
          workers[w] = '.', 0

  return time, ''.join(complete)

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
    ans = answer(sorted(in_file.readlines()), num_workers=5, time_sub=0)
    print(ans)

