#!/usr/bin/env python3
#Calculate hamming distance for all combinations of lines
#Find two lines that only differ by one character
#Output the common characters in those two lines

def hamming(s1, s2):
  "Hamming distance. Sum of number of differing characters"
  assert len(s1) == len(s2)
  return sum(c1 != c2 for c1, c2 in zip(s1, s2))

the_two_lines = []

with open('02.input', 'r') as in_list:
  in_list_lines = in_list.readlines()
for l in in_list_lines:
  #print(l)
  #Compare with all the other lines (and itself)
  for c in in_list_lines:
    if hamming(l, c) == 1:
      print(l)
      the_two_lines.append(l)

print('Common characters:', end=' ')
print(''.join([c1 for c1, c2 in zip(the_two_lines[0], the_two_lines[1]) if c1 == c2 ]))



