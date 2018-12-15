#!/usr/bin/env python3
import pytest
DAY='14'

def gen_recipes(elf1, elf2, in_str):
  new_recipe_number = int(in_str[elf1]) + int(in_str[elf2])
  if new_recipe_number < 10:
    new_recipes_l = [new_recipe_number]
  else:
    new_recipes_l = [new_recipe_number // 10, new_recipe_number % 10] # Split into the first 10 base digit and second.
  return in_str+''.join(str(r) for r in new_recipes_l)

def move_elves(recipes, elf1, elf2):
  if elf1 == elf2:
    import pdb;pdb.set_trace()
    # ze komen op dezelfde positie terecht. wat te doen!? FIXME
  steps1 = 1 + int(recipes[elf1])
  steps2 = 1 + int(recipes[elf2])
  return ((elf1+steps1) % len(recipes), (elf2+steps2) % len(recipes))

def print_recipes_elves(recipes, elf1, elf2):
  retval = ''
  for i, c in enumerate(recipes):
    if i == elf1:
      retval += '({})'.format(c)
    elif i == elf2:
      retval += '[{}]'.format(c)
    else:
      retval += ' {} '.format(c)
  return retval
    

def get_state(recipes, steps):
  elf1 = 0
  elf2 = 1
  recipes_str = print_recipes_elves(recipes, elf1, elf2)
  #print(recipes_str)
  for i in range(1, steps+1):
    recipes = gen_recipes(elf1, elf2, recipes)
    elf1, elf2 = move_elves(recipes, elf1, elf2)
    recipes_str = print_recipes_elves(recipes, elf1, elf2)
    print(recipes_str)
  print(recipes_str)
  return recipes_str

def next_ten(recipes, nr_recipes, steps=0):
  'get scores of the ten recipes after nr_recipes have been completed'
  state = ''
  while len(state) < (nr_recipes+10):
    print('Steps: {}'.format(steps))
    print(len(state))
    state = get_state(recipes, steps).replace(' ', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '')
    steps += 1
  print('State: {}'.format(state))

  return state[nr_recipes:nr_recipes+10]

@pytest.fixture
def example_input():
  return '37'

@pytest.fixture
def testresult():
  with open('{}.testresult'.format(DAY), 'r') as in_file:
    return in_file.read().split('\n')

def test_first_runs(example_input, testresult):
  print('')
  elf1 = 0
  elf2 = 1
  initial_state = print_recipes_elves(example_input, elf1, elf2)
  print(initial_state)
  assert initial_state == testresult[0]
  recipes = gen_recipes(elf1, elf2, example_input)
  assert recipes == '3710'
  assert move_elves(recipes, elf1, elf2) == (0,1)
  state_1 = print_recipes_elves(recipes, elf1, elf2)
  print(state_1)
  assert state_1 == testresult[1]

def test_get_state(example_input, testresult):
  for i, l in enumerate(testresult):
    if not l:
      break
    assert get_state(example_input, i) == l

def test_next_ten(example_input):
  assert next_ten(example_input, 5) == '0124515891'
  assert next_ten(example_input, 9) == '5158916779'
  assert next_ten(example_input, 18) == '9251071085'
  assert next_ten(example_input, 2018, 1516) == '5941429882'

if __name__ == '__main__':
  puzzle_input = '990941'
  print('Answer: {}'.format(next_ten(puzzle_input, len(puzzle_input))))

