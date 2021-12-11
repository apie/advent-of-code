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

def answer(lines, STEPS=100000, NROWS=10, NCOLS=10):
    print('')
    n_flashes = 0
    octos = []
    for line in map(str.strip, lines):
        octos.append(list(int(o) for o in list(line)))
    print_octos(octos)
    for step in range(1, STEPS+1):
        print(f'----- {step=} ------')
        flashers = set()
        #increase level for each octo
        for i in range(NROWS):
            for j in range(NCOLS):
                octos[i][j] += 1

        #increase level of octos adjacent to flashers
        def increase_adjacent(i, j):
            if j > 0:#check left
                if octos[i][j-1] <= 9 and not (i,j-1) in flashers:
#                    print('increasing.left')
                    octos[i][j-1] += 1
            if i > 0 and j > 0:#check left diag
                if octos[i-1][j-1] <= 9 and not (i-1,j-1) in flashers:
#                    print('increasing.left diag')
                    octos[i-1][j-1] += 1
            if i > 0:#check top
                if octos[i-1][j] <= 9 and not (i-1,j) in flashers:
#                    print('increasing.top')
                    octos[i-1][j] += 1
            if i > 0 and j < NCOLS-1:#check right diag
                if octos[i-1][j+1] <= 9 and not (i-1,j+1) in flashers:
#                    print('increasing.right diag')
                    octos[i-1][j+1] += 1
            if j < NCOLS-1:#check right
                if octos[i][j+1] <= 9 and not (i,j+1) in flashers:
                    #print('increasing.right')
                    octos[i][j+1] += 1
            if i < NROWS-1 and j < NCOLS-1:#check bottom right diag
                if octos[i+1][j+1] <= 9 and not (i+1,j+1) in flashers:
                    #print('increasing.bottom right ')
                    octos[i+1][j+1] += 1
            if i < NROWS-1:#check bottom
                if octos[i+1][j] <= 9 and not (i+1,j) in flashers:
                    #print('increasing.bottom')
                    octos[i+1][j] += 1
            if i < NROWS-1 and j > 0:#check bottom left diag
                if octos[i+1][j-1] <= 9 and not (i+1,j-1) in flashers:
                    #print('increasing.bottom left')
                    octos[i+1][j-1] += 1
        def flash(n):
            flashed = False
            #any with level > 9 : FLASH
            for i in range(NROWS):
                for j in range(NCOLS):
                    if octos[i][j] > 9:
                        flashed = True
#                        print('flashing ',i,j)
                        n += 1
                        if (i,j) not in flashers:#only allowed once per step
                            increase_adjacent(i, j)
                        flashers.add((i,j))
                        #reset this one
                        octos[i][j] = 0
            no_flashes = not flashed
            return no_flashes, n

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

