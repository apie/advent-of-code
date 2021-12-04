#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
from d4a import *

def answer(lines):
    lines = list(map(str.strip, lines))
    draws, boards = parse_board(lines)
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
            if bingo(b, direct_return=False):
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
    score = sum_board(boards[w]) * nr_just_called
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
    assert ans == 17388
    print(ans)


