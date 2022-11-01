#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def answer(lines):
    for line in map(str.strip, lines):
        print(line)

@pytest.mark.parametrize('inp, expected', [
#    ('', 1),
])
def test_answer_literals(inp, expected):
    assert answer([inp]) == expected


@pytest.mark.parametrize('testfileno, expected', [
#    (1, 1),
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

