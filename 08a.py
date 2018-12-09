#!/usr/bin/env python3
import pytest


def prep_input(in_lines):
  prepped_input = []
  for line in in_lines:
    for char in line.split():
      prepped_input.append(int(char.strip()))
  return prepped_input
  
def parse_nodes(in_list, nodes=None, nr_iter=None):
  print('looping: ',nr_iter)
  if not nodes:
    nodes = []
  i = 0
  while True:
    print('iteration ',i)
    try:
      nr_childs = next(in_list)
    except StopIteration:
      return nodes 
    print('Nr_childs: ',nr_childs)
    nr_metadata = next(in_list)
    print('Nr_metadata: ',nr_metadata)
    childs = []
    if nr_childs > 0:
      childs = parse_nodes(in_list, nr_iter=nr_childs)
    print('Childs: ',childs)
    metadata = []
    for nm in range(nr_metadata):
      metadata.append(next(in_list))
    print('Metadata: ',metadata)
    nodes.append(dict(
      childs=childs,
      meta=metadata
    ))
    i += 1
    if nr_iter and i >= nr_iter:
      break
  #never reached?
  return nodes

def sum_meta(nodes, meta_total=0):
  for node in nodes:
    for m in node['meta']:
      meta_total += m
    if 'childs' in node:
      meta_total = sum_meta(node['childs'], meta_total)
  return meta_total

@pytest.fixture
def example_input():
  return '''
  2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
  '''
  #1 3 0 1 9 1 2 3
  #0 3 1 2 3 0 1 9
  #0 3 1 2 3

def test_most(example_input):
  prepped_input = prep_input(example_input.split('\n'))
  print(prepped_input)
  nodes = parse_nodes(iter(prepped_input))
  import pprint
  pprint.pprint(nodes, depth=100)
  assert nodes == [
    dict(childs=[ #A
        dict(meta=[10,11,12], childs=[]),#B
        dict(childs=[#C
          dict(meta=[99], childs=[])#D
          ],
          meta=[2],
        )
      ],
      meta=[1,1,2],
    )
  ]
  assert sum_meta(nodes) == 138


if __name__ == '__main__':
  with open('08.input', 'r') as in_file:
    prepped_input = prep_input(in_file.readlines())
  nodes = parse_nodes(iter(prepped_input))
  import pprint
  pprint.pprint(nodes, depth=100)
  print('Answer: ',sum_meta(nodes))


