#!/usr/bin/env python3
from itertools import cycle

total = 0
reached = {}
reached[total] = 1
with open('01.input', 'r') as in_list:
  in_list_lines = in_list.readlines()
  for l in cycle(in_list_lines):
    #print(l)
    num = int(l.replace('+', ''))
    #print(num)
    total += num
    if total not in reached:
      reached[total] = 1
    else:
      print('Reached {} twice'.format(total))
      break

print('Total: {}'.format(total))
  
  
