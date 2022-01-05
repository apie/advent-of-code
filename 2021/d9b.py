#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
from collections import defaultdict

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
                low_points.append((y,x))

    print('low points')
    print(low_points)
    #Each low point is the lowest point of a basin. From the low point, explore the neighbours
    basins = defaultdict(list)
    visited = defaultdict(dict)
    def explore(y, x):
#        print('exploring',x,y)
        for i in range(4):
            thisx = thisy = None
            if i == 0 and x>0: #left
                thisx = x-1
                thisy = y
            if i == 1 and x<maxx: #right
                thisx = x+1
                thisy = y
            if i == 2 and y>0: #top
                thisx = x
                thisy = y-1
            if i == 3 and y<maxy: #bottom
                thisx = x
                thisy = y+1
            if thisx is None and thisy is None:
                continue
            if not visited.get(thisy, {}).get(thisx) and m[thisy][thisx] < 9:
                basins[p].append(m[thisy][thisx])
                visited[thisy][thisx] = True
                explore(thisy, thisx)
    for p in low_points:
        y, x = p
        visited[y][x] = True
        basins[p].append(m[y][x])
        explore(y, x)
    
#    print('basins')
#    from pprint import pprint
#    pprint(basins)



    # Find the three largest basins and multiply their sizes
    basin_lens = []
    for basin in basins.values():
        basin_lens.append(len(basin))
#        print(len(basin))
    basin_lens = sorted(basin_lens)[-3:]
#    print(basin_lens)
    ans = 1
    for l in basin_lens:
        ans *= l
    return ans

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 1134

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

