#!/usr/bin/env python3
import pytest
DAY='14'

@pytest.fixture
def example_input():
  return '37'

def answer(recipes, needle):
  recipes = [int(c) for c in recipes]
  elf1 = 0
  elf2 = 1
  i = 0
  while not needle in ''.join([str(r) for r in recipes[-len(needle)-1:]]):
    if i % 1000 == 0:
      print(i)
    new_recipe_number = int(recipes[elf1]) + int(recipes[elf2])
    recipes.extend((new_recipe_number,) if new_recipe_number < 10 else divmod(new_recipe_number,10)) # Split into the first 10 base digit and second.
    steps1 = 1 + int(recipes[elf1])
    steps2 = 1 + int(recipes[elf2])
    elf1, elf2 = ((elf1+steps1) % len(recipes), (elf2+steps2) % len(recipes))
    i += 1
  #print(len(recipes))
  return len(recipes) - len(needle)

def test_answer(example_input):
  assert answer(example_input, '51589') == 9
  assert answer(example_input, '101245') == 4
  assert answer(example_input, '01245') == 5
  assert answer(example_input, '92510') == 18
  assert answer(example_input, '59414') == 2018

if __name__ == '__main__':
  initial_recipes = example_input()
  puzzle_input = '990941'
  print('Answer: {}'.format(answer(initial_recipes, puzzle_input)))
  print('or this minus one')
