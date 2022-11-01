#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
from collections import Counter
VOWELS = 'aeiou'

def is_nice(string):
    c = Counter(string)
    vowelcount = sum(
        c[vowel]
        for vowel in VOWELS
    )
    if vowelcount < 3:
        return False

    if 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string:
        return False

    for i, c in enumerate(string):
        try:
            if string[i+1] == c:
                # repeating letter
                return True
        except IndexError:
            pass
    return False
        

def answer(lines):
    return sum(
        is_nice(string)
        for string in map(str.strip, lines)
    )


@pytest.mark.parametrize('testfileno, expected', [
    (1, 1),
    (2, 1),
    (3, 0),
    (4, 0),
    (5, 0),
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

