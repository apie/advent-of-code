#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
from hashlib import md5


def answer(lines):
    secret_key = next(map(str.strip, lines))
    lines.close()
    number = 1
    # Start mining AdventCoins
    while not md5(f'{secret_key}{number}'.encode()).hexdigest()[:6] == '000000':
        number += 1
    return number


@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 6742839

@pytest.fixture
def example_input2():
    return fileinput.input(F_NAME + '.test.2')

def test_answer2(example_input2):
    assert answer(example_input2) == 5714438

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

