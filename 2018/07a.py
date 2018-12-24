#!/usr/bin/env python3
import pytest
import re
DAY='07'

class Tree():
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
  def __str__(self):
    return '{} ({}, {})'.format(self.data, self.left or '', self.right or '')

def find(tree, name):
  if not tree:
    return
  if tree.data == name:
    return tree
  return find(tree.left, name) or find(tree.right, name)

def answer(in_lines):
  nodes = dict()
  for in_line in in_lines:
    #print('['+in_line.strip()+']')
    m = re.match(r'Step (.) must be finished before step (.) can begin.', in_line.strip())
    if not m:
      continue
    first = m.group(1)
    second = m.group(2)
    fn = None
    for n in nodes.values():
      fn = find(n, first)
      if fn:
        break
    if not fn:
      fn = nodes.get(first)
    if not fn:
      fn = Tree(first)
      nodes[first] = fn
    fc = find(fn, second)
    if not fc:
      fc = nodes.get(second)
      if fc:
        del nodes[second]
      else:
        fc = Tree(second)
    if not fn.left:
      fn.left = fc
    elif not fn.right:
      fn.right = fc
    #print(fn)
    #print(fc)
  for name, node in nodes.items():
    print(name)
    print(node)


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
  answer(sorted(example_input.split('\n')))
  #assert answer(sorted(example_input.split('\n'))) == 'CABDFE'

if __name__ == '__main__':
  with open('{}.input'.format(DAY), 'r') as in_file:
    print(answer(sorted(in_file.readlines())))


