#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

mapje={
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}

def answer(lines):
    answer = 0
    for line in map(str.strip, lines):
        lans = ''
        print(line)
        curword = ''
        break2 = False
        for c in line:
            if break2: break
            curword += c
            for w in mapje.keys():
                if w in curword:
                    lans += mapje[w]
                    break2 = True  # found digit at start of line.

        curword = ''
        break2 = False
        for c in reversed(line):
            if break2: break
            curword += c
            rcurword = ''.join(reversed(curword))
            for w in mapje.keys():
                if w in rcurword:
                    lans += mapje[w]
                    break2 = True  # found digit at end of line.

        print(lans)
        answer += int(lans)
    print(answer)
    return answer


@pytest.mark.parametrize('testfileno, expected', [
    (2, 281),
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

