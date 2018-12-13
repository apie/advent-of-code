#!/usr/bin/env python3
import pytest
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
CARTSEQUENCE='LSR'
COLLISION='X'

class Cart():
  def __init__(self, c, x, y):
    self.c = c
    self.track = VERT if c in [CARTUP, CARTDOWN] else HORIZ
    self.x = x
    self.y = y
    self.turns = iter(CARTSEQUENCE)
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
    next(self.turns)
    print(self.turns)
    #TODO
 
class Map():
  def __init__(self, in_lines):
    self.map_l = in_lines
    self.carts = []
    for y, l in enumerate(self.map_l):
      for x, c in enumerate(l):
        #print(x,c)
        if c in CARTS:
          self.carts.append(Cart(c, x, y))

  def collision(self, new_pos):
      a=list(self.map_l[new_pos[1]]);a[new_pos[0]]=COLLISION
      self.map_l[new_pos[1]]=''.join(a);

  def tick(self):
    cart_positions = set()
    for cart in self.carts:
      old_pos = cart.get_pos()
      print('Voor: ',cart.get_pos())
      cart.move()
      print(self.map_l)
      #import pdb;pdb.set_trace()
      a=list(self.map_l[old_pos[1]]);a[old_pos[0]]=cart.track;
      self.map_l[old_pos[1]]=''.join(a);
      print(self.map_l)

      new_pos = cart.get_pos()
      print('Na: ',new_pos)
      if new_pos in cart_positions:
        return self.collision(new_pos)
      cart_positions.add(new_pos)
      new_track_char = self.map_l[new_pos[1]][new_pos[0]]
      cart.track = new_track_char
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
      print(self.map_l)
  def get_map(self):
    return '\n'.join(self.map_l)

@pytest.fixture
def example_input_1():
  with open('{}.input.test.1'.format(DAY), 'r') as in_file:
    return in_file.read().split('\n')

def test_answer(example_input_1):
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
  return
  assert m==1
  while True:
    m.tick()
  assert m==1

if __name__ == '__main__':
  with open('{}.input'.format(DAY), 'r') as in_file:
    print(answer(in_file.readlines()))


