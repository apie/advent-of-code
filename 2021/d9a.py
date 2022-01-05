#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def answer(lines):
    print()
    m = []
    for line in map(str.strip, lines):
        if not line:
            continue
        print(line)
        m.append(list(map(int, list(line))))
    maxx = len(m[0])-1
    maxy = len(m)-1
#    print(f'{maxy=}')
    low_points = []
    for y in range(maxy+1):
        for x in range(maxx+1):
            this = m[y][x]
#            print(x, y, this)
            low = 0
            maxlow = 4
            if x>0:    low += this < m[y  ][x-1] #left
            else: maxlow -= 1
            if x<maxx: low += this < m[y  ][x+1] #right
            else: maxlow -= 1
            if y>0:    low += this < m[y-1][x  ] #top
            else: maxlow -= 1
            if y<maxy: low += this < m[y+1][x  ] #bottom
            else: maxlow -= 1
            if low == maxlow:
                low_points.append(this)

#    print(low_points)

    # The risk level of a low point is 1 plus its height. Return the sum.
    return sum(low_points)+len(low_points)

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 15

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

