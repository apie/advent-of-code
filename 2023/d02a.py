#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
import re

bagcontent = dict(
    red=12,
    green=13,
    blue=14,
)

def answer(lines):
    answer = 0
    for line in map(str.strip, lines):
        print(line)
        gameid = re.match(r'Game (\d+):', line)[1]
        for setje in line.split(':')[1].strip().split(';'):
            bagc = bagcontent.copy()
            for cube in setje.split(','):
                for color in bagc.keys():
                    if color in cube:
                        bagc[color] -= int(re.match(r'\d+', cube.strip())[0])
                        break
            if any(v < 0 for v in bagc.values()):
                print(gameid, 'is impossible')
                gameid = 0
                break
        answer += int(gameid)
    return answer

@pytest.mark.parametrize('testfileno, expected', [
    (1, 8),
])
def test_answer_testfiles(testfileno, expected):
    assert answer(fileinput.input(f"{F_NAME}.test.{testfileno}")) == expected

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    assert ans > 119
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

