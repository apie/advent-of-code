#!/usr/bin/env python3
import pytest
from itertools import cycle
from operator import attrgetter

DAY='13'
VERT='|'
HORIZ='-'
DIAGDU='/'
DIAGUD='\\'
INTER='+'

CARTUP='^'
CARTDOWN='v'
CARTLEFT='<'
CARTRIGHT='>'
CARTS =(CARTUP, CARTDOWN, CARTLEFT, CARTRIGHT)
CARTSL='L'
CARTSS='S'
CARTSR='R'
CARTSEQUENCE=(CARTSL, CARTSS, CARTSR)
CRASH='X'

class Cart():
  def __init__(self, c, x, y):
    self.c = c
    self.track = VERT if c in [CARTUP, CARTDOWN] else HORIZ
    self.x = x
    self.y = y
    self.turns = cycle(CARTSEQUENCE)
  def move(self):
    if self.c == CARTUP:
      self.y -= 1
    elif self.c == CARTDOWN:
      self.y += 1
    elif self.c == CARTLEFT:
      self.x -= 1
    elif self.c == CARTRIGHT:
      self.x += 1
  def get_pos(self):
    return (self.x, self.y)
  def turn(self):
    n_turn = next(self.turns)
    if self.c == CARTUP:
      if n_turn == CARTSL:
        self.c = CARTLEFT
      elif n_turn == CARTSR:
        self.c = CARTRIGHT
    elif self.c == CARTDOWN:
      if n_turn == CARTSL:
        self.c = CARTRIGHT
      elif n_turn == CARTSR:
        self.c = CARTLEFT
    elif self.c == CARTLEFT:
      if n_turn == CARTSL:
        self.c = CARTDOWN
      elif n_turn == CARTSR:
        self.c = CARTUP
    elif self.c == CARTRIGHT:
      if n_turn == CARTSL:
        self.c = CARTUP
      elif n_turn == CARTSR:
        self.c = CARTDOWN
 
class Map():
  def __init__(self, in_lines):
    self.map_l = in_lines
    self.carts = []
    self.locations = []
    for y, l in enumerate(self.map_l):
      for x, c in enumerate(l):
        if c in CARTS:
          self.carts.append(Cart(c, x, y))

  def crash(self, new_pos):
      a=list(self.map_l[new_pos[1]]);a[new_pos[0]]=CRASH
      self.map_l[new_pos[1]]=''.join(a);

  def tick(self):
    cart_positions = set()
    cart_positions_tracks = dict()
    for cart in sorted(self.carts, key=attrgetter('x', 'y')):
      old_pos = cart.get_pos()
      #print('Voor: ',cart.get_pos())
      cart.move()
      #print(self.map_l)
      a=list(self.map_l[old_pos[1]]);a[old_pos[0]]=cart.track;
      self.map_l[old_pos[1]]=''.join(a);
      #print(self.map_l)

      new_pos = cart.get_pos()
      #print('Na: ',new_pos)
      new_track_char = self.map_l[new_pos[1]][new_pos[0]]
      cart.track = new_track_char
      cart_positions_tracks[new_pos] = cart.track
      if new_track_char == DIAGDU: #/
        if cart.c == CARTUP:
          cart.c = CARTRIGHT 
        elif cart.c == CARTLEFT:
          cart.c = CARTDOWN 
        elif cart.c == CARTDOWN:
          cart.c = CARTLEFT
        elif cart.c == CARTRIGHT:
          cart.c = CARTUP
      elif new_track_char == DIAGUD: #\
        if cart.c == CARTUP:
          cart.c = CARTLEFT 
        elif cart.c == CARTLEFT:
          cart.c = CARTUP 
        elif cart.c == CARTDOWN:
          cart.c = CARTRIGHT
        elif cart.c == CARTRIGHT:
          cart.c = CARTDOWN
      elif new_track_char == INTER: #+
        cart.turn()
      a=list(self.map_l[new_pos[1]]);a[new_pos[0]]=cart.c
      self.map_l[new_pos[1]]=''.join(a);
      if new_pos in cart_positions:
        cart.c = CRASH
        cart.track = cart_positions_tracks[new_pos]
        self.crash(new_pos)
        continue
      cart_positions.add(new_pos)
      #print(self.map_l)

  def get_map(self):
    return '\n'.join(self.map_l)

  def get_crash_location(self):
    self.locations.clear()
    for y, l in enumerate(self.map_l):
      for x, c in enumerate(l):
        if c == CRASH:
          self.locations.append((x, y))
    if len(self.locations) == 1:
      return self.locations[0]
    return self.locations

  def remove_crashed_carts(self):
    to_remove = []
    for cl in self.locations:
      for c in self.carts:
        if c.get_pos() == cl:
          pos = c.get_pos()
          print('Removing: ', pos)
          #import pdb;pdb.set_trace()
          if c.track not in CARTS:
            a=list(self.map_l[pos[1]]);a[pos[0]]=c.track
            self.map_l[pos[1]]=''.join(a);
          to_remove.append(c)
    for c in to_remove:
      self.carts.remove(c)

@pytest.fixture
def example_input_3():
  with open('{}.input.test.3'.format(DAY), 'r') as in_file:
    return in_file.read().split('\n')

def test_example_3(example_input_3):
  print()
  m = Map(example_input_3[:7])
  print(m.get_map())
  print('Nr of carts: ',len(m.carts))
  for i in range(1, 4):
    print('TICK')
    m.tick()
    print([c.get_pos() for c in sorted(m.carts, key=attrgetter('x', 'y'))])
    print('Crash at: ', m.get_crash_location())
    m.remove_crashed_carts()
    print(m.get_map())
    print('Nr of carts: ',len(m.carts))
    print([c.get_pos() for c in m.carts])
    assert m.map_l == example_input_3[i*8:i*8+7]
  assert len(m.carts) == 1
  assert m.carts[0].get_pos() == (6,4)

if __name__ == '__main__':
  with open('{}.input'.format(DAY), 'r') as in_file:
    in_lines = in_file.read().split('\n')
  print()
  m = Map(in_lines)
  print(m.get_map())
  i = 0
  while not len(m.carts) == 1:
    i += 1
    m.tick()
    m.remove_crashed_carts()
    print('TICK {:3}, CARTS: {}'.format(i, len(m.carts)))
    #print(m.get_map())
  print(m.carts[0].get_pos())


