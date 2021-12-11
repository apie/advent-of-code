#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]


def print_octos(oc):
    octo_str = ''
    for l in oc:
        line = ''.join(map(str, l))
        octo_str += line.replace('0', ' ') + '\n'
    print(octo_str)
    print('')

def answer(lines, STEPS=1000, NROWS=10, NCOLS=10):
    def parse_input(lines):
        return [
            list(int(o) for o in list(line))
            for line in map(str.strip, lines)
        ]

    def increase_octo_levels():
        for i in range(NROWS):
            for j in range(NCOLS):
                octos[i][j] += 1

    def flash(n):
        def increase_adjacent(i, j):
            def increase(r, c, direction):
                if octos[r][c] <= 9 and not (r,c) in flashers:
#                    print(f'increasing {direction}')
                    octos[r][c] += 1

            if j > 0:
                increase(i, j-1, 'left')
            if i > 0 and j > 0:
                increase(i-1, j-1, 'top left diag')
            if i > 0:
                increase(i-1, j, 'top')
            if i > 0 and j < NCOLS-1:
                increase(i-1, j+1, 'top right diag')
            if j < NCOLS-1:
                increase(i, j+1, 'right')
            if i < NROWS-1 and j < NCOLS-1:
                increase(i+1, j+1, 'bottom right diag')
            if i < NROWS-1:
                increase(i+1, j, 'bottom')
            if i < NROWS-1 and j > 0:
                increase(i+1, j-1, 'bottom left diag')

        # ------------------
        flashed = False
        for i in range(NROWS):
            for j in range(NCOLS):
                #any with level > 9 : FLASH
                if octos[i][j] > 9:
                    flashed = True
#                        print('flashing ',i,j)
                    n += 1
                    if (i,j) not in flashers:#only allowed once per step
                        #increase level of octos adjacent to flashers
                        increase_adjacent(i, j)
                    flashers.add((i,j))
                    #reset this one
                    octos[i][j] = 0
        return not flashed, n
    #--------------

    print('')
    n_flashes = 0
    octos = parse_input(lines)
    print_octos(octos)
    for step in range(1, STEPS+1):
        print(f'----- {step=} ------')
        flashers = set()
        #increase level for each octo
        increase_octo_levels()
        flash_done = False
        while not flash_done:
            flash_done, n_flashes = flash(n_flashes)
        #octo can only flash once per step
        print_octos(octos)
        #return step at which all the octopuses flash
        if sum(
            sum(c for c in l)
            for l in octos
        ) == 0:
            return step

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 195

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)

