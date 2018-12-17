#!/usr/bin/env python3
import pytest
DAY='14'

@pytest.fixture
def example_input():
  return '37'

def answer(recipes, nr_recipes):
  """We need to extend the list of recipes to the length of the desired nr + 10. Then we need to find the last 10 recipes."""
  recipes = [int(c) for c in recipes]
  elf1 = 0
  elf2 = 1
  i = 0
  while len(recipes) < nr_recipes + 10:
    if i % 1000 == 0:
      print(i)
    new_recipe_number = int(recipes[elf1]) + int(recipes[elf2])
    recipes.extend((new_recipe_number,) if new_recipe_number < 10 else divmod(new_recipe_number,10)) # Split into the first 10 base digit and second.
    steps1 = 1 + int(recipes[elf1])
    steps2 = 1 + int(recipes[elf2])
    elf1, elf2 = ((elf1+steps1) % len(recipes), (elf2+steps2) % len(recipes))
    i += 1
  return ''.join([str(r) for r in recipes[nr_recipes:][0:10]])

def test_answer(example_input):
  assert answer(example_input, 3) == '0101245158'
  assert answer(example_input, 9) == '5158916779'
  assert answer(example_input, 5) == '0124515891'
  assert answer(example_input, 18) == '9251071085'
  assert answer(example_input, 2018) == '5941429882'

if __name__ == '__main__':
  initial_recipes = example_input()
  puzzle_input = 990941
  print('Answer: {}'.format(answer(initial_recipes, puzzle_input)))

