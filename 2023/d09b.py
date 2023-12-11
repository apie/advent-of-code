#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def get_diff(lijst):
    val = None
    diffs = []
    for dig in lijst:
        if val is not None:
            diffs.append(dig - val)
        val = dig
    return diffs

def answer(lines):
    answer = 0
    for line in map(str.strip, lines):
        diffs = [
            list(map(int, line.split()))
        ]
        while not all(d == 0 for d in diffs[-1]):
            diffs.append(get_diff(diffs[-1]))

        diffs.reverse()
        prevvalue = 0
        for d in diffs:
            prevvalue = d[0] - prevvalue
        answer += prevvalue
    return answer

@pytest.mark.parametrize('testfileno, expected', [
    (1, 2),
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

