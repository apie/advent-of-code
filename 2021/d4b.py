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
    print(f'{sum_of_unmarked=}')
    return sum_of_unmarked * nr_just_called
    
def bingo(b):
    has_bingo = False
    #check horizontal bingo
    for i in range(5):
        rowstart = i*5
        row=b[rowstart:rowstart+5]
        if sum(row) == -5:
            has_bingo = True
    #check vertical bingo
    for i in range(5):
        colstart = i
        col = [b[colstart+(0*5)], b[colstart+(1*5)] , b[colstart+(2*5)] , b[colstart+(3*5)] , b[colstart+(4*5)] ]
        if sum(col) == -5:
            has_bingo = True
    #Keep going until all the boards are checked and only then return if bingo was called
    return has_bingo
    
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
        start = (iboard*6) + 1
        board = lines[start:start+5]
        boards.append([
            int(b)
            for br in board
            for b in br.replace('  ', ' ').split(' ')
        ])

    print('parsed:')
    print_boards(boards)
    def draw():
        drawed = draws.pop(0)
        print(f'{drawed=}')
        has_bingo = []
        for ib, b in enumerate(boards):
            try:
                i = b.index(drawed)
                b[i] = -1
            except ValueError:
                #not on board
                pass
            if bingo(b):
                has_bingo.append(ib)
                print(f'{has_bingo=}')
        if has_bingo:
            return has_bingo, drawed
        return [], None

    #play
    winners = set()
    nr_just_called = None
    last_board_won = False
    #find last board to win
    while last_board_won is False:
        won, nr_just_called = draw()
        for w in won:
            if w not in winners:
                print(f'New bingo on board {w}')
                winners.add(w)
                print_boards(boards)
                print(winners)
                last_board_won = len(winners) == len(boards)
                if last_board_won:
                    break
    print_boards(boards)
    print(f'Getting score for board {w}')
    score = get_score_for_board(boards[w], nr_just_called)
    print(f'{score=}')
    #return final score of that board
    return score

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 1924

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    assert ans != 7308 #wrong. too low

