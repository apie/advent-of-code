#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
from itertools import cycle
import re

def answer(lines):
    instructions = cycle(next(lines).strip())
    elements = {}
    next(lines)
    for line in map(str.strip, lines):
        print(line)
        node, left, right = re.match(r'(...) = \((...), (...)\)', line).groups()
#        breakpoint()
        elements[node] = (left, right)
    element = 'AAA'
    steps = 0
    while element != 'ZZZ':
        steps += 1
        element = elements[element]
        instruction = next(instructions)
        if instruction == 'L':
            element = element[0]
        else:
            element = element[1]
#    print(elements)
    print(steps)
    return steps

@pytest.mark.parametrize('testfileno, expected', [
    (1, 2),
    (2, 6),
])
def test_answer_testfiles(testfileno, expected):
    assert answer(fileinput.input(f"{F_NAME}.test.{testfileno}")) == expected

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

