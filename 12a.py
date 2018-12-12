#!/usr/bin/env python3
import pytest
DAY=12

class Plants():
  def __init__(self, in_lines):
    self.generation = 0
    lines = iter(in_lines)
    initial_state = next(lines).replace('initial state: ', '')
    self.pots = {i:s for i, s in enumerate(initial_state)
      if s == '#'
    }
    self.rules = {
      r.split('=>')[0].strip():r.split('=>')[1].strip()
      for r in lines if r and r.split('=>')[1].strip() == '#'
    }
  def gen(self):
    pots_new = {}
    for p in range(min(self.pots.keys())-4, max(self.pots.keys())+1+4):
      key = '{}{}{}{}{}'.format(
        '#' if p-2 in self.pots else '.',
        '#' if p-1 in self.pots else '.',
        '#' if p-0 in self.pots else '.',
        '#' if p+1 in self.pots else '.',
        '#' if p+2 in self.pots else '.',
      )
      if key in self.rules:
        pots_new[p] = '#'
        pots_new_str = ''.join(['#' if i in pots_new else '.'
          for i in range(min(pots_new.keys()), max(pots_new.keys())+1)])
    self.pots = pots_new
    self.generation += 1

  def print_pots(self):
    return ''.join(['#' if i in self.pots else '.'
      #for i in range(min(self.pots.keys()), max(self.pots.keys())+1)])
      for i in range(min(-3, *self.pots.keys()), max(35, *self.pots.keys())+1)])

  def sum_pots(self):
    return sum(self.pots.keys())

@pytest.fixture
def example_result():
  with open('12.testresult', 'r') as in_file:
    return in_file.read().split('\n')

@pytest.fixture
def example_input():
  with open('12.input.test', 'r') as in_file:
    return in_file.read().split('\n')

def test_answer(example_input, example_result):
  plants = Plants(example_input)
  print('Rules: ',plants.rules)
  print('Pots after {} generations: {}'.format(plants.generation, plants.print_pots()))
  assert '0: '+plants.print_pots() == example_result[2].strip()
  for i in range(1, 20+1):
    plants.gen()
    print('Pots after {} generations: {}'.format(plants.generation, plants.print_pots()))
    assert '{:2}: {}'.format(i, plants.print_pots()) == example_result[2+i]
  assert plants.sum_pots() == 325

if __name__ == '__main__':
  with open('{:02}.input'.format(DAY), 'r') as in_file:
    in_lines = in_file.read().split('\n')
  plants = Plants(in_lines)
  print('Pots after {} generations: {}'.format(plants.generation, plants.print_pots()))
  for i in range(1, 20+1):
    plants.gen()
    print('Pots after {} generations: {}'.format(plants.generation, plants.print_pots()))
  print('Answer: {}'.format(plants.sum_pots()))

