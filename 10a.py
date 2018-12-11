#!/usr/bin/env python3
import pytest
import re
from collections import defaultdict

class Point():
  def __init__(self, args):
    x, y, ax, ay = args
    self.x=int(x)
    self.y=int(y)
    self.ax=int(ax)
    self.ay=int(ay)
    self.time=0
  def step(self, step=1):
    self.time += step 
    self.x += self.ax*step
    self.y += self.ay*step
  def get_pos(self):
    return (self.x, self.y)
  def get_a(self):
    return (self.ax, self.ay)

class Grid():
  def __init__(self):
    self.g = defaultdict(dict)
    self.max_x = self.max_y = self.min_x = self.min_y = 0
    self.points = []
  def add_point(self, p):
    self.points.append(p)
    self.calc_extremes(p)
    self._set_point(p)
  def reset_extremes(self):
    self.max_x = self.min_x = self.max_y = self.min_y = 0
  def calc_extremes(self, p):
    self.max_x = max(self.max_x, p.x)
    self.min_x = min(self.min_x, p.x)
    self.max_y = max(self.max_y, p.y)
    self.min_y = min(self.min_y, p.y)
  def _set_point(self, p):
    self.g[p.x][p.y] = '#'
  def _clear_point(self, p):
    try:
      del self.g[p.x][p.y]
    except KeyError:
      pass
  def step_points(self, steps=1, crop=False):
    if crop:
      self.reset_extremes()
    for p in self.points:
      self._clear_point(p)
      p.step(steps)
      self._set_point(p)
      if crop:
        self.calc_extremes(p)
  def get_constellation(self, axis=False):
    const = []
    for y in range(self.min_y, self.max_y+1):
      cx = []
      for x in range(self.min_x, self.max_x+1):
        try:
          cx.append(self.g[x][y])
        except KeyError:
          if axis and x==0 and y==0:
            cx.append('+')
          elif axis and x==0:
            cx.append('|')
          elif axis and y==0:
            cx.append('-')
          else:
            cx.append('.')
      const.append(''.join(cx))
    return '\n'.join(const)
  def max_drawing(self):
      max_x = 0
      for y in range(self.min_y, self.max_y+1):
        for x in range(self.min_x, self.max_x+1):
          max_x = max(max_x, abs(self.g)) + max(self.g.keys())
          max_y = max(max_y, abs(self.g[x].keys())) + max(self.g[x].keys())
          #TODO


def parse_line(line):
  'Returns (x, y, ax, ay)'
  m = re.match(r'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>', line)
  if m:
    return m.groups()

def answer(in_lines):
  g = Grid()
  for l in in_lines:
    if l.strip():
      g.add_point(Point(parse_line(l.strip())))
  return g
  #determine the correct stop times. if found. return those prints.

@pytest.fixture
def example_input():
  return '''
  position=< 9,  1> velocity=< 0,  2>
  position=< 7,  0> velocity=<-1,  0>
  position=< 3, -2> velocity=<-1,  1>
  position=< 6, 10> velocity=<-2, -1>
  position=< 2, -4> velocity=< 2,  2>
  position=<-6, 10> velocity=< 2, -2>
  position=< 1,  8> velocity=< 1, -1>
  position=< 1,  7> velocity=< 1,  0>
  position=<-3, 11> velocity=< 1, -2>
  position=< 7,  6> velocity=<-1, -1>
  position=<-2,  3> velocity=< 1,  0>
  position=<-4,  3> velocity=< 2,  0>
  position=<10, -3> velocity=<-1,  1>
  position=< 5, 11> velocity=< 1, -2>
  position=< 4,  7> velocity=< 0, -1>
  position=< 8, -2> velocity=< 0,  1>
  position=<15,  0> velocity=<-2,  0>
  position=< 1,  6> velocity=< 1,  0>
  position=< 8,  9> velocity=< 0, -1>
  position=< 3,  3> velocity=<-1,  1>
  position=< 0,  5> velocity=< 0, -1>
  position=<-2,  2> velocity=< 2,  0>
  position=< 5, -2> velocity=< 1,  2>
  position=< 1,  4> velocity=< 2,  1>
  position=<-2,  7> velocity=< 2, -2>
  position=< 3,  6> velocity=<-1, -1>
  position=< 5,  0> velocity=< 1,  0>
  position=<-6,  0> velocity=< 2,  0>
  position=< 5,  9> velocity=< 1, -2>
  position=<14,  7> velocity=<-2,  0>
  position=<-3,  6> velocity=< 2, -1>
  '''

def test_answer(example_input):
  g = answer(example_input.split('\n'))
  grid_size = (g.min_x, g.max_x, g.min_y, g.max_y)
  assert grid_size == (-6, 15, -4, 11)
  print('Grid size: ', grid_size)
  c = g.get_constellation()
  print(g.get_constellation(True))
  print()
  # t0
  coords = [(p.get_pos(), p.get_a()) for p in g.points]
  coords.sort()
  print(coords)
  print(len(coords))
  assert c == '''
........#.............
................#.....
.........#.#..#.......
......................
#..........#.#.......#
...............#......
....#.................
..#.#....#............
.......#..............
......#...............
...#...#.#...#........
....#..#..#.........#.
.......#..............
...........#..#.......
#...........#.........
...#.......#..........
'''.strip()
  g.step_points()
  c = g.get_constellation()
  print(g.get_constellation(True))
  print()
  # t1
  coords = [(p.get_pos(), p.get_a()) for p in g.points]
  coords.sort()
  print(coords)
  print(len(coords))
  assert c == '''
......................
......................
..........#....#......
........#.....#.......
..#.........#......#..
......................
......#...............
....##.........#......
......#.#.............
.....##.##..#.........
........#.#...........
........#...#.....#...
..#...........#.......
....#.....#.#.........
......................
......................
'''.strip()
  g.step_points()
  c = g.get_constellation()
  print(g.get_constellation(True))
  print()
  # t2
  coords = [(p.get_pos(), p.get_a()) for p in g.points]
  coords.sort()
  print(coords)
  print(len(coords))
  assert c == '''
......................
......................
......................
..............#.......
....#..#...####..#....
......................
........#....#........
......#.#.............
.......#...#..........
.......#..#..#.#......
....#....#.#..........
.....#...#...##.#.....
........#.............
......................
......................
......................
'''.strip()
  g.step_points()
  c = g.get_constellation()
  print(g.get_constellation(True))
  print()
  # t3
  coords = [(p.get_pos(), p.get_a()) for p in g.points]
  coords.sort()
  print(coords)
  print(len(coords))
  assert c == '''
......................
......................
......................
......................
......#...#..###......
......#...#...#.......
......#...#...#.......
......#####...#.......
......#...#...#.......
......#...#...#.......
......#...#...#.......
......#...#..###......
......................
......................
......................
......................
'''.strip()
  g.step_points()
  c = g.get_constellation()
  print(g.get_constellation(True))
  print()
  # t4
  coords = [(p.get_pos(), p.get_a()) for p in g.points]
  coords.sort()
  print(coords)
  print(len(coords))
  assert c == '''
......................
......................
......................
............#.........
........##...#.#......
......#.....#..#......
.....#..##.##.#.......
.......##.#....#......
...........#....#.....
..............#.......
....#......#...#......
.....#.....##.........
...............#......
...............#......
......................
......................
'''.strip()
  #TODO ook nog strippen (whitespace eromheen weghalen

if __name__ == '__main__':
  with open('10.input', 'r') as in_file:
    g = answer(in_file.readlines())
  g.print_grid()
  g.step_points(crop=True)
  g.print_grid()
  #TODO kleinste bounding box dat moet iets zijn.


