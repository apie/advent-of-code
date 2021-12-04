#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def print_boards(boards):
    for b in boards:
        print_board(b)
def print_board(b):
    for i in range(5):
        print(' '.join(f'{c:>2}' for c in b[i*5:(i*5)+5]))
    print('-'*10)

def sum_board(b):
    return sum(n for n in b if n != -1)
 
def bingo(b, direct_return=True):
    has_bingo = False
    #check horizontal bingo
    for i in range(5):
        rowstart = i*5
        row=b[rowstart:rowstart+5]
        if sum(row) == -5:
            has_bingo = True
            if direct_return: return has_bingo
    #check vertical bingo
    for i in range(5):
        colstart = i
        col = [b[colstart+(0*5)], b[colstart+(1*5)] , b[colstart+(2*5)] , b[colstart+(3*5)] , b[colstart+(4*5)] ]
        if sum(col) == -5:
            has_bingo = True
            if direct_return: return has_bingo
    #Keep going until all the boards are checked and only then return if bingo was called
    return has_bingo

def parse_board(lines):
    draws = list(map(int, lines.pop(0).split(',')))
    nboards = len(lines) // 6
    print(draws)
    print(nboards)
    boards = []
    for iboard in range(nboards):
        start = (iboard*6) + 1
        board = lines[start:start+5]
        boards.append([
            int(b)
            for br in board
            for b in br.replace('  ', ' ').split(' ')
        ])
    print('parsed:')
    print_boards(boards)
    return draws, boards

def answer(lines):
    lines = list(map(str.strip, lines))
    draws, boards = parse_board(lines)
    def draw():
        print('drawing..')
        drawed = draws.pop(0)
        print(f'{drawed=}')
        for ib, b in enumerate(boards):
            try:
                i = b.index(drawed)
                b[i] = -1
            except ValueError:
                #not on board
                pass
            if bingo(b):
                return ib, drawed
        return None, None

    #play
    won = None
    nr_just_called = None
    while won is None:
        won, nr_just_called = draw()
    print(f'Bingo on board {won}')
    #find first board to win
    print_boards(boards)
    score = sum_board(boards[won]) * nr_just_called
    print(f'{score=}')
    #return final score of that board
    return score

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 4512

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    assert ans == 14093
    print(ans)

