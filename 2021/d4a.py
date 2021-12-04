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

def get_score_for_board(b, nr_just_called):
    sum_of_unmarked = sum(n for n in b if n != -1)
    return sum_of_unmarked * nr_just_called
    
class BingoE(Exception):
    pass

def bingo(b):
    #check horizontal bingo
#    breakpoint()
    for i in range(5):
        rowstart = i*5
        if sum(b[rowstart:rowstart+5]) == -5:
            raise BingoE('bingo')
    #check vertical bingo
    for i in range(5):
        colstart = i
        col = [b[colstart+(0*5)], b[colstart+(1*5)] , b[colstart+(2*5)] , b[colstart+(3*5)] , b[colstart+(4*5)] ]
        print(col)
#        breakpoint()
        if sum(col) == -5:
            raise BingoE('bingo')
    
def answer(lines):
    draws = None
    boards = []
    lines = list(map(str.strip, lines))
    draws = list(map(int, lines[0].split(',')))
    del lines[0]
    nboards = len(lines) // 6
    print(draws)
    print(nboards)
    for iboard in range(nboards):
#        breakpoint()
        start = (iboard*6) + 1
        board = lines[start:start+5]
        parsed_board = [int(b)
        for br in board
        for b in br.replace('  ', ' ').split(' ')
        ]
        boards.append(parsed_board)

    print('parsed:')
    print_boards(boards)
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
#            print_board(b)
            try:
                bingo(b)
            except BingoE:
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
    score = get_score_for_board(boards[won], nr_just_called)
    print(f'{score=}')
    #return final score of that board
    return score

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 4512

if __name__ == '__main__':
    print(answer(fileinput.input(F_NAME + '.input')))

