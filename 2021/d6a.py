#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def daypasses(fishes):
    for i in range(len(fishes)):
        fishes[i] -= 1
        if fishes[i] == -1:
            fishes.append(8)
            fishes[i] = 6
#    print(fishes)
    return fishes

def answer(lines):
    fishes = list(int(f) for f in list(lines)[0].strip().split(','))
    print(fishes)
    for x in range(80):
        fishes = daypasses(fishes)
        print(x, len(fishes))
    return len(fishes)

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 5934

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)

