#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

LETTERS = {
    k.replace(' ', '').strip(): v
    for k, v in {
    '''
    .##..
    #..#.
    #..#.
    ####.
    #..#.
    #..#.
    .....
    ''': 'A',
    '''
    ###..
    #..#.
    ###..
    #..#.
    #..#.
    ###..
    .....
    ''': 'B',
    '''
    .##..
    #..#.
    #....
    #....
    #..#.
    .##..
    .....
    ''': 'C',
    '''
    ..##.
    ...#.
    ...#.
    ...#.
    #..#.
    .##..
    .....
    ''': 'J',
    '''
    #..#.
    #.#..
    ##...
    #.#..
    #.#..
    #..#.
    .....
    ''': 'K',
    '''
    ###..
    #..#.
    #..#.
    ###..
    #....
    #....
    .....
    ''': 'P',
    }.items()
}


def split_grid_into_chars(grid, maxx, maxy):
    #letter width is 4 + 1 space character
    chars = []
    for start in range(maxx//5):
        char = ''
        startx = start*5
        for y in range(maxy+1):
            for x in range(startx, startx+5):
                is_dash = grid.get(x) and grid[x].get(y)
#                    print('#' if is_dash else '.', end='')
                char += '#' if is_dash else '.'
#                print()
            char += '\n'
        chars.append(char)
    return chars

def answer(lines):
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
#        print('Folding Y')
        for y in range(maxy+1):
            for x in range(maxx+1):
                is_dash = grid.get(x) and grid[x].get(y)
                if is_dash and y>foldy-1:
                    ynew = foldy - y + foldy
#                    print(f'Folding {x},{y} to {x,ynew}')
                    grid[x][y] = False
                    grid[x][ynew] = True
        return grid

    def fold_x(grid, foldx):
#        print('Folding X')
        for y in range(maxy+1):
            for x in range(maxx+1):
                is_dash = grid.get(x) and grid[x].get(y)
                if is_dash and x>foldx-1:
                    xnew = foldx - x + foldx
#                    print(f'Folding {x},{y} to {y,xnew}')
                    grid[x][y] = False
                    if not grid.get(xnew):
                        grid[xnew] = dict()
                    grid[xnew][y] = True
        return grid

    def parse_input(lines):
        maxx = maxy = 0
        folds = []
        grid = dict()
        for line in map(str.strip, lines):
            if not line:
                continue
#            print(line)
            if line.startswith('fold along'):
                if 'x' in line:
                    folds.append(('x', int(line.split('=')[1])))
                else:
                    folds.append(('y', int(line.split('=')[1])))
            else:
                x, y = map(int, line.strip().split(','))
                maxx = max(maxx, x)
                maxy = max(maxy, y)
                if not grid.get(x):
                    grid[x] = dict()
                grid[x][y] = True
        return grid, folds, maxx, maxy

    grid, fold_instructions, maxx, maxy = parse_input(lines)
#    pg(grid)
#    print(f'{fold_instructions=}, {maxx=}, {maxy=}')
    while fold_instructions:
        ins = fold_instructions.pop(0)
        direction, xy = ins
        if direction == 'y':
            grid = fold_y(grid, xy)
            maxy = xy
        else:
            grid = fold_x(grid, xy)
            maxx = xy
    pg(grid)
    print()

    chars = split_grid_into_chars(grid, maxx, maxy)
    return ''.join(LETTERS[char.strip()] for char in chars)

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)

