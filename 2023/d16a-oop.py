#!/usr/bin/env python3
import pytest
import fileinput
from io import StringIO
from os.path import splitext, abspath
import re
F_NAME = re.match(r'.+/d\d+', splitext(abspath(__file__))[0])[0]

from dataclasses import dataclass

def print_energized(energized_tiles, h, w):
    print('\033[2J\033[H')
    for y in range(h):
        for x in range(w):
            tile = '.'
            if str(Point(x,y)) in energized_tiles:
                tile = '#'
            print(tile, end='')
        print()
    print()


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Walker:
    position: Point
    direction: str

    def __add__(self, d):
        if d == 'r':
            self.position.x += 1
        elif d == 'l':
            self.position.x -= 1
        elif d == 'u':
            self.position.y -= 1
        elif d == 'd':
            self.position.y += 1

    def move(self):
        self + self.direction

    def turnright(self):
        if self.direction == 'u':
            self.direction = 'r'
        elif self.direction == 'r':
            self.direction = 'd'
        elif self.direction == 'd':
            self.direction = 'l'
        elif self.direction == 'l':
            self.direction = 'u'
        return self

    def turnleft(self):
        return self.turnright().turnright().turnright()


class Grid:

    def __init__(self, lines):
        self.grid = list(map(str.strip, lines)) # [y][x]

    def tile(self, walker):
        try:
            return self.grid[walker.position.y][walker.position.x]
        except IndexError:
            return

    def __str__(self):
        r = StringIO()
        print('', file=r)
        for y, line in enumerate(self.grid):
            for x, c in enumerate(line):
                print(c, end='', file=r)
            print(file=r)
        print('', file=r)
        return r.getvalue()


def answer(lines):
    ## cave [y][x]
    cave = Grid(lines)
    energized_tiles = set()
    energized_tiles_direction = set()

    def movebeam(w, initial=False):
        ## pos (x,y)
        if (str(w.position), w.direction) in energized_tiles_direction:
            return

        energized_tiles.add(str(w.position))
        if not initial:
            energized_tiles_direction.add((str(w.position), w.direction))
            w.move()

        if w.position.x < 0 or w.position.y < 0:
            return

        tile = cave.tile(w)
        if not tile:
            return

        if tile == '/':
            if w.direction in ('r', 'l'):
                w.turnleft()
            elif w.direction in ('u', 'd'):
                w.turnright()
        elif tile == '\\':
            if w.direction in ('r', 'l'):
                w.turnright()
            elif w.direction in ('u', 'd'):
                w.turnleft()
        elif tile == '|':
            if w.direction in ('l', 'r'):
                w.direction = 'd'
                movebeam(Walker(Point(w.position.x, w.position.y), 'u'))
        elif tile == '-':
            if w.direction in ('u', 'd'):
                w.direction = 'l'
                movebeam(Walker(Point(w.position.x, w.position.y), 'r'))

        movebeam(w)

    print(cave)
    movebeam(Walker(Point(0,0), 'r'), initial=True)
    print_energized(energized_tiles, len(cave.grid), len(cave.grid[0]))
    return len(energized_tiles)


@pytest.mark.parametrize('testfileno, expected', [
    (1, 46),
])
def test_answer_testfiles(testfileno, expected):
    print()
    assert answer(fileinput.input(f"{F_NAME}.test.{testfileno}")) == expected

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(4000)
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer() - start
    print(f'Execution time: {duration:.3f} s')

