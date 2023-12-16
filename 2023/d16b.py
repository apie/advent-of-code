#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def printenergized(energized, h, w):
    print('\033[2J\033[H')
    for y in range(h):
        for x in range(w):
            if (x,y) in energized:
                tile = '#'
            else:
                tile = '.'
            print(tile, end='')
        print()
    print()

def getenergized(cave, startpos, startdir):

    def printcave():
        print()
        for line in cave:
            print(line)
        print()


    energized = set()
    energizeddir = set()

    def movebeam(pos, dire, initial=False):
        ## pos (x,y)
        if (pos, dire) in energizeddir:
            return
        energized.add(pos)
        x, y = pos
        if initial:
            pass
        else:
            energizeddir.add((pos, dire))
            if dire == 'r':
                x += 1
            elif dire == 'l':
                x -= 1
            elif dire == 'u':
                y -= 1
            elif dire == 'd':
                y += 1
            else:
                1/0

        if x < 0 or y < 0:
            return

        try:
            tile = cave[y][x]
        except IndexError:
            return

        if tile == '.':
            pass
        elif tile == '/':
            if dire == 'r':
                dire = 'u'
            elif dire == 'l':
                dire = 'd'
            elif dire == 'u':
                dire = 'r'
            elif dire == 'd':
                dire = 'l'
        elif tile == '\\':
            if dire == 'r':
                dire = 'd'
            elif dire == 'l':
                dire = 'u'
            elif dire == 'u':
                dire = 'l'
            elif dire == 'd':
                dire = 'r'
        elif tile == '|':
            if dire == 'r':
                dire = 'd'
                movebeam((x,y), 'u')
            elif dire == 'l':
                dire = 'd'
                movebeam((x,y), 'u')
        elif tile == '-':
            if dire == 'u':
                dire = 'l'
                movebeam((x,y), 'r')
            elif dire == 'd':
                dire = 'l'
                movebeam((x,y), 'r')

#        if len(energized) % 1000 == 0:
#            printenergized(energized, len(cave), len(cave[0]))

        movebeam((x,y), dire)
                
#    printcave()

    movebeam(startpos, startdir, initial=True)

    return len(energized)


def answer(lines):
    maxenergized = 0
    ## cave [y][x]
    cave = list(map(str.strip, lines))
    options = 0
    dirs = []
    for y in range(len(cave)):
        dirs.append(' '*len(cave))
        for x in range(len(cave[0])):
            if x == 0:
                dire = 'r'
            elif y == 0:
                dire = 'd'
            elif y == len(cave)-1:
                dire = 'u'
            elif x == len(cave)-1:
                dire = 'l'
            else:
                continue
            dirstr = list(dirs[y])
            dirstr[x] = dire
            dirs[y] = ''.join(dirstr)
            maxenergized = max(
                maxenergized,
                getenergized(cave, (x,y), dire),
            )
            options += 1
    print()
    print('possible positions with direction:')
    for dir in dirs:
        print(dir)
    print('total:', options)
    return maxenergized

@pytest.mark.parametrize('testfileno, expected', [
    (1, 51),
])
def test_answer_testfiles(testfileno, expected):
    print()
    assert answer(fileinput.input(f"{F_NAME}.test.{testfileno}")) == expected

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10000)
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    assert ans != 18
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

