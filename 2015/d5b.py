#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
import re

def is_nice(string):
    if not re.match(r'.*(..).*\1', string):
        return False
    if not re.match(r'.*(.).\1', string):
        return False
    return True
        

def answer(lines):
    return sum(
        is_nice(string)
        for string in map(str.strip, lines)
    )


@pytest.mark.parametrize('inp, expected', [
    ('qjhvhtzxzqqjkmpb', 1),
    ('xxyxx', 1),
    ('uurcxstgmygtbstg', 0),
    ('ieodomkazucvgmuy', 0),
])
def test_answer_literals(inp, expected):
    assert answer([inp]) == expected


if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

