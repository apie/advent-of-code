#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath

def is_valid(number, r_min, r_max):
    number = str(number).strip()
    if not number.isnumeric() or len(number) != 6:
        return False
    inumber = int(number)
    if inumber > r_max or inumber < r_min:
        return False
    oldchar = ''
    found = False
    for c in number:
        if c == oldchar:
          found = True
          break
        oldchar = c
    if not found:
        return False
    old_d = 0
    for c in number:
        d = int(c)
        if d < old_d:
            return False
        old_d = d

    return True

def answer(in_lines):
    r = list(map(int, next(in_lines).strip().split('-')))
    return sum(is_valid(c, *r) for c in range(r[0], r[1]+1))

def test_answer():
    r = (1, 999999)
    assert is_valid(111111, *r)
    assert not is_valid(223450, *r)
    assert not is_valid(123789, *r)

if __name__ == '__main__':
    print(answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input')))

