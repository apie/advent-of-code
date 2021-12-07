#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def get_moves(positions, move_to):
    moves = 0
    for p in positions:
        moves += abs(p-move_to)
    return moves

def answer(lines, move_func=None):
    if not move_func:
        move_func = get_moves
    #find position to move to which costs the minimum amount of moves
    #and then return the number of moves
    positions = list(map(int, map(str.strip, list(lines)[0].split(','))))
    # print(positions)
    max_positions = max(positions)
    
    move_matrix = []
    #calculate the move costs for all the possible positions
    for mt in range(max(positions)+1):
        move_matrix.append(move_func(positions, mt))
    # print(f'{move_matrix=}')
    optimal_nr_of_moves = max(positions)+1 #set to invalid value
    #find optimal position
    optimal_position = move_matrix.index(min(move_matrix))
    print(f'{optimal_position=}')
    return move_matrix[optimal_position]

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    #pos 2
    assert answer(example_input) == 37

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)

