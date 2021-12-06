#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]


def answer(lines, i):
    fishes = list(int(f) for f in list(lines)[0].strip().split(','))
    #dont keep track of which ages are where, only how many fish are there of a certain age. then to pass the day we can shift
    fishbin = {}
    for xi in range(9):
        fishbin[xi] = 0
    for f in fishes:
        fishbin[f] += 1

    def passday():
        new = fishbin[0]
        fishbin[0]=fishbin[1]
        fishbin[1]=fishbin[2]
        fishbin[2]=fishbin[3]
        fishbin[3]=fishbin[4]
        fishbin[4]=fishbin[5]
        fishbin[5]=fishbin[6]
        fishbin[6]=fishbin[7]+new
        fishbin[7]=fishbin[8]
        fishbin[8]=new
#        print(fishbin)
#        print(sum(fishbin.values()))
    for d in range(i):
        passday()
    return sum(fishbin.values())

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

@pytest.mark.parametrize('i,o', [
    (0,5),
    (1,5),
    (2,6),
    (3,7),
    (4,9),
    (5,10),
    (6,10),
    (7,10),#####
    (8,10),
    (9,11),
    (10,12),
    (11,15),
    (12,17),
    (13,19),
    (14,20),#####
    (15,20),
    (16,21),
    (17,22),
    (18,26),
    (80,5934),
    (256,26984457539),
])
def test_answer(example_input, i,o):
    assert answer(example_input, i) == o

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'), 256)
    print(ans)

