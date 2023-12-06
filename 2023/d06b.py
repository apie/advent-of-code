#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
import re

def answer(lines):
    answer = 1
    print()
    times = distances = None
    for line in map(str.strip, lines):
        line = line.replace(' ', '')
        print(line)
        if not times:
            times = map(int, re.findall(r'\d+', line))
            continue
        distances = map(int, re.findall(r'\d+', line))
    for i, duration_distance in enumerate(zip(times, distances), start=1):
        duration, distance = duration_distance
        print('---race', i)
        print('duration:', duration, 'ms')
        print('record distance:', distance, 'mm')
        n_wins = 0
        for hold in range(duration+1):
            travelled = (duration-hold)*hold
#            print(hold, travelled)
            if travelled > distance:
                n_wins += 1
        print(f'{n_wins=}')
        answer *= n_wins
    return answer

@pytest.mark.parametrize('testfileno, expected', [
    (1, 71503),
])
def test_answer_testfiles(testfileno, expected):
    assert answer(fileinput.input(f"{F_NAME}.test.{testfileno}")) == expected

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

