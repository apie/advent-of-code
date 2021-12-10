#!/usr/bin/env python3
from functools import partial
from d7a import answer
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]


def get_moves_slow(positions, move_to):
    # Slow takes 2 minutes
    moves = 0
    # todo optimize
    for p in positions:
        for _ in range(abs(p-move_to)):
            moves += _+1
    return moves


def get_moves_slow2(positions, move_to):
    # Takes 28 secs
    moves = 0
    # todo optimize
    for p in positions:
        l = abs(p-move_to)
        moves += sum(range(l))+l
    return moves

# This is called a triangular number:
# https://nl.wikipedia.org/wiki/Driehoeksgetal
# https://en.wikipedia.org/wiki/Triangular_number
# sum(range(abs(p-move_to))) + abs(p-move_to)
# or
# sum(range(abs(p-move_to)+1))
# we can also calculate it like this
# 0.5n(n + 1)
#
# or / n + 1\         (n+1)!
#    |      |   =>  -----------
#    \   2  /       2! * (n-1)!
from functools import lru_cache
@lru_cache()
def triangulator1(n):
    return sum(range(n+1))
# @lru_cache()
def triangulator2(n):
    return 0.5*n*(n+1)

def get_moves(positions, move_to):
    # Takes 27 secs with triangulator1
    # Takes 1 sec with triangulator2 (lru_cache not even needed)
    return sum(
        # sum(range(abs(p-move_to))) + abs(p-move_to)
        # sum(range(abs(p-move_to)+1))
        # triangulator1(abs(p-move_to))
        triangulator2(abs(p-move_to))
        for p in positions
    )


@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')


def test_answer(example_input):
    # pos 5
    assert answer(example_input, move_func=get_moves) == 168


if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'), move_func=get_moves)
    print(ans)
