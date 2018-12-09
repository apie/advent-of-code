#!/usr/bin/env python3
import pytest

def prep_input(in_lines):
  prepped_input = []
  for line in in_lines:
    for char in line.split():
      prepped_input.append(int(char.strip()))
  return prepped_input
  
def parse_nodes(in_list, nodes=None, nr_iter=None):
  if not nodes:
    nodes = []
  i = 0
  while True:
    try:
      nr_childs = next(in_list)
    except StopIteration:
      return nodes 
    nr_metadata = next(in_list)
    childs = []
    if nr_childs > 0:
      childs = parse_nodes(in_list, nr_iter=nr_childs)
    metadata = []
    for nm in range(nr_metadata):
      metadata.append(next(in_list))
    nodes.append(dict(
      childs=childs,
      meta=metadata
    ))
    i += 1
    if nr_iter and i >= nr_iter:
      break
  #never reached?
  return nodes

def nodevalue(node):
  if len(node['childs']):
    return sum(nodevalue(node['childs'][m-1])
      for m in node['meta'] if m <= len(node['childs']))
  else:
    return sum(m for m in node['meta'])

@pytest.fixture
def example_input():
  return '''
  2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
  '''

def test_most(example_input):
  prepped_input = prep_input(example_input.split('\n'))
  nodes = parse_nodes(iter(prepped_input))
  assert nodevalue(nodes[0]) == 66 #A
  assert nodevalue(nodes[0]['childs'][0]) == 33 #B
  assert nodevalue(nodes[0]['childs'][1]['childs'][0]) == 99 #D
  assert nodevalue(nodes[0]['childs'][1]) == 0 #C


if __name__ == '__main__':
  with open('08.input', 'r') as in_file:
    prepped_input = prep_input(in_file.readlines())
  nodes = parse_nodes(iter(prepped_input))
  print('Answer: ',nodevalue(nodes[0]))


