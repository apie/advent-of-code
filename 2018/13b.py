#!/usr/bin/env python3
import pytest
from itertools import cycle

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
    for cart in self.carts:
      old_pos = cart.get_pos()
      #print('Voor: ',cart.get_pos())
      cart.move()
      #print(self.map_l)
      a=list(self.map_l[old_pos[1]]);a[old_pos[0]]=cart.track;
      self.map_l[old_pos[1]]=''.join(a);
      #print(self.map_l)

      new_pos = cart.get_pos()
      #print('Na: ',new_pos)
      if new_pos in cart_positions:
        cart.c = CRASH
        cart.track = cart_positions_tracks[new_pos]
        self.crash(new_pos)
        continue
      cart_positions.add(new_pos)
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
      #print(self.map_l)

  def get_map(self):
    return '\n'.join(self.map_l)

  def get_crash_location(self):
    for y, l in enumerate(self.map_l):
      for x, c in enumerate(l):
        if c == CRASH:
          return (x, y)

  def remove_crashed_carts(self):
    for c in self.carts:
      if c.c == CRASH:
        new_pos = c.get_pos()
        #import pdb;pdb.set_trace()
        a=list(self.map_l[new_pos[1]]);a[new_pos[0]]=c.track
        self.map_l[new_pos[1]]=''.join(a);
        self.carts.remove(c)

@pytest.fixture
def example_input_1():
  with open('{}.input.test.1'.format(DAY), 'r') as in_file:
    return in_file.read().split('\n')

@pytest.fixture
def example_input_2():
  with open('{}.input.test.2'.format(DAY), 'r') as in_file:
    return in_file.read().split('\n')

@pytest.fixture
def example_input_3():
  with open('{}.input.test.3'.format(DAY), 'r') as in_file:
    return in_file.read().split('\n')

def test_example_1(example_input_1):
  print()
  m = Map(example_input_1[:7])
  print(m.get_map())
  m.tick()
  print('TICK')
  print(m.get_map())
  # Skip intermediate results in the example_input_1
  assert m.map_l == example_input_1[1*16:1*16+7]
  m.tick()
  print('TICK')
  print(m.get_map())
  assert m.map_l == example_input_1[2*16:2*16+7]

def test_example_2(example_input_2):
  print()
  m = Map(example_input_2[:6])
  print(m.get_map())
  for i in range(1, 15):
    m.tick()
    print('TICK')
    print(m.get_map())
    assert m.map_l == example_input_2[i*7:i*7+6]
  assert m.get_crash_location() == (7,3)

def test_example_3(example_input_3):
  print()
  m = Map(example_input_3[:7])
  print(m.get_map())
  for i in range(1, 4):
    m.tick()
    print('Crash at: ', m.get_crash_location())
    m.remove_crashed_carts()
    m.remove_crashed_carts()
    print('TICK')
    print(m.get_map())
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
  while not m.get_crash_location():
    i += 1
    m.tick()
    print('TICK {:3}'.format(i))
    #print(m.get_map())
  print(m.get_crash_location())


