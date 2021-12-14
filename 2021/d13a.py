#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]


def answer(lines, fold_all=False):
    maxx = maxy = 0
    def pg(grid):
        dash_count = 0
        for y in range(maxy+1):
            for x in range(maxx+1):
                is_dash = grid.get(x) and grid[x].get(y)
                if is_dash:
                    dash_count += 1
                print('#' if is_dash else '.', end='')
            print()
        return dash_count

    def fold_y(grid, foldy):
        print('Folding Y')
        for y in range(maxy+1):
            for x in range(maxx+1):
                is_dash = grid.get(x) and grid[x].get(y)
                if is_dash and y>foldy-1:
                    ynew = foldy - y + foldy
                    print(f'Folding {x},{y} to {x,ynew}')
                    grid[x][y] = False
                    grid[x][ynew] = True
        return grid

    def fold_x(grid, foldx):
        print('Folding X')
        for y in range(maxy+1):
            for x in range(maxx+1):
                is_dash = grid.get(x) and grid[x].get(y)
                if is_dash and x>foldx-1:
                    xnew = foldx - x + foldx
                    print(f'Folding {x},{y} to {y,xnew}')
                    grid[x][y] = False
                    if not grid.get(xnew):
                        grid[xnew] = dict()
                    grid[xnew][y] = True
        return grid

    def parse_input(lines):
        maxx = maxy = 0
        foldx = foldy = 0
        fold_found = False
        grid = dict()
        for line in map(str.strip, lines):
            if not line:
                continue
            print(line)
            if line.startswith('fold along'):
                if fold_found:
                    continue # only search for the first fold
                if not fold_all:
                    fold_found = True
                if 'x' in line:
                    foldx = int(line.split('=')[1])
                else:
                    foldy = int(line.split('=')[1])
            else:
                x, y = map(int, line.strip().split(','))
                maxx = max(maxx, x)
                maxy = max(maxy, y)
                if not grid.get(x):
                    grid[x] = dict()
                grid[x][y] = True
        return grid, foldx, foldy, maxx, maxy

    grid, foldx, foldy, maxx, maxy = parse_input(lines)
    dc = pg(grid)
    print(f'{foldx=}, {foldy=}, {maxx=}, {maxy=}')
    print(dc)
    if foldy:
        grid = fold_y(grid, foldy)
    dc = pg(grid)
    print(dc)
    if foldx:
        grid = fold_x(grid, foldx)
    dc = pg(grid)
    print(dc)
    return dc

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 17
def test_answer_foldall(example_input):
    assert answer(example_input, fold_all=True) == 16

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)

