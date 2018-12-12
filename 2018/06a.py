#!/usr/bin/env python3
import pytest
import string
from math import *
from coordinates import Coordinate as coord
from collections import defaultdict
from operator import itemgetter

def num_to_char(num):
  return chr(97+num)

def manhattan_distance(a, b):
  return abs(a.x - b.x) + abs(a.y - b.y)

def test_manhattan_distance():
  assert manhattan_distance(coord(x=1, y=1), coord(x=2, y=1)) == 1
  assert manhattan_distance(coord(x=1, y=1), coord(x=3, y=1)) == 2
  assert manhattan_distance(coord(x=1, y=1), coord(x=3, y=2)) == 3
  assert manhattan_distance(coord(x=2, y=1), coord(x=3, y=2)) == 2

def calculate_closest_distances(grid_size, in_lines):
  distances_grid = defaultdict(dict)
  for y in range(1, grid_size[1]+1):
    for x in range(1, grid_size[0]+1):
      distances = dict()
      for i, p in enumerate(in_lines):
        distances[i] = manhattan_distance(coord(x=x, y=y), p)
      closest_points = sorted(distances.items(), key=itemgetter(1))
      closest_point = closest_points[0]
      indicator = num_to_char(closest_point[0]).lower()
      if closest_points[0][1] == closest_points[1][1]:
        # The two points are at the same distance
        indicator = '.'
      #print('{} ({})'.format(num_to_char(closest_point[0]).upper(), closest_point[1]))
      distances_grid[x][y] = num_to_char(closest_point[0]).upper() if closest_point[1] == 0 else indicator

  return distances_grid
 
def prepare_input(input_str):
  in_lines = []
  for l in input_str.split('\n'):
    l = l.strip()
    if not l:
      continue
    x_str, y_str = l.strip().split(',')
    x = int(x_str.strip())
    y = int(y_str.strip())
    in_lines.append(coord(x=x, y=y))
  return in_lines

def max_size(in_lines):
  return (max(p.x for p in in_lines), max(p.y for p in in_lines)) 

def get_distances(input_str, print_grid=False):
  prepared_input = prepare_input(input_str)
  print('Max size')
  grid_size = max_size(prepared_input)
  print(grid_size)
  print()

  # Print start grid
  if print_grid:
    xy = defaultdict(dict)
    for i, p in enumerate(prepared_input):
      xy[p.x][p.y] = i
    for y in range(1, grid_size[1]+1):
      for x in range(1, grid_size[0]+1):
        try:
          print(num_to_char(xy[x][y]).upper(), end='')
        except KeyError:
          print('.', end='')
      print()
    print()

  distances = calculate_closest_distances(grid_size, prepared_input)
  return grid_size, distances

def size_largest_area(grid_size, distances):
  # Chars at the edge extend infinite so we need to remove those
  remove_chars = set()
  for y in range(1, grid_size[1]+1):
    remove_chars.add(distances[1][y])
  for x in range(1, grid_size[0]+1):
    remove_chars.add(distances[x][1])

  areas = dict()
  for y in range(1, grid_size[1]+1):
    for x in range(1, grid_size[0]+1):
      areas[distances[x][y].lower()] = 0
      if distances[x][y] in remove_chars:
        distances[x][y] == ''

  # Calculate area per char
  for y in range(1, grid_size[1]+1):
    for x in range(1, grid_size[0]+1):
      areas[distances[x][y].lower()] += 1

  return sorted(areas.items(), key=itemgetter(1), reverse=True)[0]

@pytest.fixture
def example_input():
  return '''
  1, 1
  1, 6
  8, 3
  3, 4
  5, 5
  8, 9
  '''

def print_grid(grid):
  for y in range(1, max(grid[1].keys())+1):
    for x in range(1, max(grid.keys())+1):
      print(grid[x][y], end='')
    print()
  print()

def test_size_largest_area(example_input):
  grid_size, distances = get_distances(example_input, True)
  print_grid(distances)
  assert distances == {
    1: {1: 'A', 2: 'a', 3: 'a', 4: '.', 5: 'b', 6: 'B', 7: 'b', 8: 'b', 9: 'b'},
    2: {1: 'a', 2: 'a', 3: 'd', 4: 'd', 5: '.', 6: 'b', 7: 'b', 8: 'b', 9: 'b'},
    3: {1: 'a', 2: 'd', 3: 'd', 4: 'D', 5: 'd', 6: '.', 7: '.', 8: '.', 9: '.'},
    4: {1: 'a', 2: 'd', 3: 'd', 4: 'd', 5: 'e', 6: 'e', 7: 'e', 8: 'e', 9: 'f'},
    5: {1: '.', 2: 'e', 3: 'e', 4: 'e', 5: 'E', 6: 'e', 7: 'e', 8: 'e', 9: 'f'},
    6: {1: 'c', 2: 'c', 3: 'c', 4: 'e', 5: 'e', 6: 'e', 7: 'e', 8: 'f', 9: 'f'},
    7: {1: 'c', 2: 'c', 3: 'c', 4: 'c', 5: 'e', 6: 'e', 7: 'f', 8: 'f', 9: 'f'},
    8: {1: 'c', 2: 'c', 3: 'C', 4: 'c', 5: 'c', 6: '.', 7: 'f', 8: 'f', 9: 'F'}
  }
  assert size_largest_area(grid_size, distances) == ('e', 17)


if __name__ == '__main__':
  with open('06.input', 'r') as in_list:
    grid_size, distances = get_distances(in_list.read())
  #print_grid(distances)
  print('nu size')
  print(size_largest_area(grid_size, distances))


