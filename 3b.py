#!/usr/bin/env python3
#pip install coordinates
from coordinates import Coordinate
import pytest

def non_overlapping_squares(in_list_lines):
  covered = dict()
  id_set = set()
  for line in in_list_lines:
    line_id=int(line.split('@')[0].strip().replace('#', ''))
    left=int(line.split('@')[1].split(':')[0].strip().split(',')[0])
    top=int(line.split('@')[1].split(':')[0].strip().split(',')[1])
    wide=int(line.split(':')[1].strip().split('x')[0])
    tall=int(line.split(':')[1].strip().split('x')[1])

    id_set.add(line_id)

    c = Coordinate(x=left,y=top)
    for point_x in range(1, wide+1):
      for point_y in range(1, tall+1):
        x = c.x + point_x
        y = c.y + point_y
        xy_str = '{},{}'.format(x, y)
        # Save id 
        lines = covered.get(xy_str, [])
        lines.append(line_id)
        covered[xy_str] = lines
  for coord, ids in covered.items():
    if len(ids) > 1:
      for id_str in ids:
        if id_str in id_set:
          id_set.remove(id_str)
  return id_set


@pytest.fixture
def example_input():
  return '''
  #1 @ 1,3: 4x4
  #2 @ 3,1: 4x4
  #3 @ 5,5: 2x2
  '''

def test_non_overlapping_squares(example_input):
  assert non_overlapping_squares(example_input.strip().split('\n')) == {3}


if __name__ == '__main__':
  with open('3.input', 'r') as in_list:
    print(non_overlapping_squares(in_list.readlines()))

