#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]


def print_octos(oc, step):
    octo_str = ''
    for l in oc:
        line = ''.join(map(str, l))
        octo_str += line.replace('0', ' ') + '\n'
    print(octo_str)
    print('')
    return
    #TODO remove these asserts when doing the real thing
    if step == 0:
        assert octo_str.strip() == '''
        5483143223
        2745854711
        5264556173
        6141336146
        6357385478
        4167524645
        2176841721
        6882881134
        4846848554
        5283751526
        '''.replace(' ','').strip()
    if step == 1:
        assert octo_str.strip() == '''
        6594254334
        3856965822
        6375667284
        7252447257
        7468496589
        5278635756
        3287952832
        7993992245
        5957959665
        6394862637
        '''.replace(' ','').strip()
    if step == 2:
        assert octo_str.strip() == '''
        8807476555
        5089087054
        8597889608
        8485769600
        8700908800
        6600088989
        6800005943
        0000007456
        9000000876
        8700006848
        '''.replace(' ','').replace('0', ' ').strip()

def answer(lines, STEPS=100, NROWS=10, NCOLS=10):
    print('')
    n_flashes = 0
    octos = []
    for line in map(str.strip, lines):
#        print(line)
        octos.append(list(int(o) for o in list(line)))
#    print(octos)
    print_octos(octos, 0)
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
                        print('flashing ',i,j)
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
            print(flash_done)
        #octo can only flash once per step
        print_octos(octos, step)
    print(n_flashes)
    #return number of flashes after 100 steps
    return n_flashes

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')
@pytest.fixture
def example_input_simple():
    return fileinput.input(F_NAME + '.simple.test')

def test_answer_simple(example_input_simple):
    assert answer(example_input_simple, STEPS=2, NROWS=5, NCOLS=5) == 9

def test_answer0(example_input):
    assert answer(example_input, STEPS=2) == 35
def test_answer1(example_input):
    assert answer(example_input, STEPS=10) == 204
def test_answer(example_input):
    assert answer(example_input) == 1656

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)

