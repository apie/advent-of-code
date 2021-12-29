#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
import networkx as nx
from d15a import answer as lowest_total_risk

def answer(lines):
    print()
    lines = list(lines)
    origmaxy = maxy = len(lines)-1
    origmaxx = maxx = len(lines[0].strip())-1
    maxx = 5*(maxx+1) -1
    maxy = 5*(maxy+1) -1
    newlines = []
    #create new segments to the right, increasing with one over and over
    for line in map(str.strip, lines):
        incr = 0
        newline = []
        for i, c in enumerate(line*5):
            newc = int(c)+incr
            if newc > 9: newc -= 9
            newline.append(newc)
            incr = (i+1) // (origmaxx+1)
        newlines.append(''.join(map(str, newline)))
    assert len(newlines[0]) == maxx+1
    #increase segment to the bottom, just increasing all the numbers by one
    print(len(newlines))
    newlinesb = []
    for x in range(1, 5):
        for line in map(str.strip, list(newlines)):
            newline = []
            for i, c in enumerate(line):
                newc = int(c)+x
                if newc > 9: newc -= 9
                newline.append(newc)
            newlinesb.append(''.join(map(str, newline)))
    newlines.extend(newlinesb)
    assert len(newlines) == maxy+1
    return lowest_total_risk(newlines)

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer_10x10x5(example_input):
    assert answer(example_input) == 315

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')


