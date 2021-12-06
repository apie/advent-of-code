#!/usr/bin/env python3
from collections import defaultdict
import pprint
import cmath
import math
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

covered = defaultdict(list)


def iscovered(x, y):
    return covered.get(x, []).count(y)


def plot(max_x, max_y):
    total_dangerous = 0
    for y in range(int(max_y)+1):
        for x in range(int(max_x)+1):
            if c := iscovered(x, y):
                if c >= 2:
                    total_dangerous += 1
                print(c, end='')
            else:
                print('.', end='')
        print('')
    return total_dangerous


def answer(lines):
    max_x = max_y = 0
    for line in map(str.strip, lines):
        print(line)
        point1, point2 = line.split(' -> ')
        r, j = point1.split(',')
        point1 = complex(int(r), int(j))
        r, j = point2.split(',')
        point2 = complex(int(r), int(j))
        max_x = max([max_x, point1.real, point2.real])
        max_y = max([max_y, point1.imag, point2.imag])

        vect = point2-point1
        print(vect)
        print(abs(vect))
        radius, angle = cmath.polar(vect)
        deg = math.degrees(angle)
        if abs(deg) % 180 == 0:
            print('horizontal line', vect)
            for x in range(int(abs(vect)) + 1):
                if point1.real < point2.real:
                    covered[point1.real + x].append(point1.imag)
                else:
                    covered[point2.real + x].append(point2.imag)
        elif abs(deg) % 45 == 0 and not abs(deg) % 90 == 0:
            print('diagonal line', vect, deg)
            # since it is strict diagonal we can step x and y simultaneously and with the same amount
            # but we have 4 possible directions for the vector
            if deg == 45.0:  # |/
                for xy in range(int(vect.real)+1):
                    covered[point1.real + xy].append(point1.imag + xy)
            elif deg == 135.0:  # \|
                for xy in range(int(abs(vect.real))+1):
                    covered[point1.real - xy].append(point1.imag + xy)
            elif deg == -135.0:  # /|
                for xy in range(int(abs(vect.real))+1):
                    covered[point1.real - xy].append(point1.imag - xy)
            elif deg == -45.0:  # |\
                for xy in range(int(vect.real)+1):
                    covered[point1.real + xy].append(point1.imag - xy)
        else:
            print('vertical line', vect)
            for y in range(int(abs(vect)) + 1):
                if point1.imag < point2.imag:
                    covered[point1.real].append(point1.imag + y)
                else:
                    covered[point2.real].append(point2.imag + y)
    # pprint.pprint(covered)
    # print(max_x, max_y)
    return plot(max_x, max_y)


@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')


def test_answer(example_input):
    assert answer(example_input) == 12


if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)
