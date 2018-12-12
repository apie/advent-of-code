#!/usr/bin/env python3

total = 0
with open('01.input', 'r') as in_list:
  for l in in_list.readlines():
    #print(l)
    num = int(l.replace('+', ''))
    #print(num)
    total += num

print('Total: {}'.format(total))
  
  
