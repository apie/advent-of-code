#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def answer(lines):
    highest = list()
    s = 0
    for line in map(str.strip, lines):
#        print(line)
        if line == '':
            highest.append(s)
            s = 0
            continue
        s += int(line)
    highest.append(s)
    s = 0
    return sum(sorted(highest, reverse=True)[:3])

def test_answer():
    example_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".splitlines()
    assert answer(example_input) == 45_000

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

