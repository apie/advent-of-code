#!/usr/bin/env python3
from collections import Counter
#Get number of lines wich contain letters with a frequency of 2
#Get number of lines wich contain letters with a frequency of 3
#Multiply those numbers

two_count = three_count = 0
with open('02.input', 'r') as in_list:
  in_list_lines = in_list.readlines()
for l in in_list_lines:
  counter = Counter(l)
  #print(l)
  #print(counter)
  two_count += any([k for k, v in counter.items() if v == 2])
  three_count += any([k for k, v in counter.items() if v == 3])

print('Two: {}, three: {}'.format(two_count, three_count))
print('Checksum: {}'.format(two_count * three_count))

  
