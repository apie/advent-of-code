#!/usr/bin/env python3
#pip install coordinates
from coordinates import Coordinate
import pytest

def overlapping_squares(in_list_lines):
  covered = dict()
  for line in in_list_lines:
    line_id=int(line.split('@')[0].strip().replace('#', ''))
    left=int(line.split('@')[1].split(':')[0].strip().split(',')[0])
    top=int(line.split('@')[1].split(':')[0].strip().split(',')[1])
    wide=int(line.split(':')[1].strip().split('x')[0])
    tall=int(line.split(':')[1].strip().split('x')[1])

    c = Coordinate(x=left,y=top)
    for point_x in range(1, wide+1):
      for point_y in range(1, tall+1):
        x = c.x + point_x
        y = c.y + point_y
        xy_str = '{},{}'.format(x, y)
        # Increase counter on every point. If the point is missing initialize it.
        covered[xy_str] = covered.get(xy_str, 0) + 1

  return {coord for coord, freq in covered.items() if freq >= 2}

@pytest.fixture
def example_input():
  return '''
  #1 @ 1,3: 4x4
  #2 @ 3,1: 4x4
  #3 @ 5,5: 2x2
  '''

def test_overlapping_squares(example_input):
  assert overlapping_squares(example_input.strip().split('\n')) == {
    '4,4',
    '5,4',
    '4,5',
    '5,5',
  }


if __name__ == '__main__':
  with open('03.input', 'r') as in_list:
    print(len(overlapping_squares(in_list.readlines())))
