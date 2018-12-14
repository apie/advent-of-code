#!/usr/bin/env python3
import pytest
DAY='14'

def gen_recipes(elf1, elf2, in_str, rounds):
  in_recipes = [int(s) for s in in_str]
  recipes = in_recipes

  new_recipe_number = in_recipes[elf1] + in_recipes[elf2]
  if new_recipe_number < 10:
    new_recipes_l = [new_recipe_number]
  else:
    new_recipes_l = [new_recipe_number // 10, new_recipe_number % 10] # Split into the first 10 base digit and second.
  recipes += new_recipes_l
  return ''.join(str(r) for r in recipes)

def move_elves(recipes, elf1, elf2):
  steps1 = 1 + int(recipes[elf1])
  steps1 %= len(recipes)
  steps2 = 1 + int(recipes[elf1])
  steps2 %= len(recipes)
  return (elf1+steps1, elf2+steps2)

def print_recipes_elves(recipes, elf1, elf2):
  retval = ''
  for i, c in enumerate(recipes):
    if i == elf1:
      retval += '({})'.format(c)
    elif i == elf2:
      retval += '[{}]'.format(c)
    else:
      #if retval.endswith(']') or retval.endswith(')'):
      #  retval += ' '
      retval += ' {} '.format(c)
  return retval
    

def next_ten():
  pass

@pytest.fixture
def example_input():
  return '37'

@pytest.fixture
def testresult():
  with open('{}.testresult'.format(DAY), 'r') as in_file:
    return in_file.read().split('\n')

def test_answer(example_input, testresult):
  print('')
  elf1 = 0
  elf2 = 1
  initial_state = print_recipes_elves(example_input, elf1, elf2)
  print(initial_state)
  assert initial_state == testresult[0]
  recipes = gen_recipes(elf1, elf2, example_input, 1)
  assert recipes == '3710'
  assert move_elves(recipes, elf1, elf2) == (0,1)
  state_1 = print_recipes_elves(recipes, elf1, elf2)
  print(state_1)
  assert state_1 == testresult[1]
  assert next_ten(example_input, 5) == '0124515891'

if __name__ == '__main__':
  with open('{}.input'.format(DAY), 'r') as in_file:
    print(answer(in_file.readlines()))


