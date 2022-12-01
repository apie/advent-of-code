#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def answer(lines):
    highest = 0
    s = 0
    for line in map(str.strip, lines):
        print(line)
        if line == '':
            highest = max(s, highest)
            s = 0
            continue
        s += int(line)
    return highest

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
    assert answer(example_input) == 24_000

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

