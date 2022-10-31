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


@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 1

@pytest.fixture
def example_input2():
    return fileinput.input(F_NAME + '.test.2')

def test_answer2(example_input2):
    assert answer(example_input2) == 1

@pytest.fixture
def example_input3():
    return fileinput.input(F_NAME + '.test.3')

def test_answer3(example_input3):
    assert answer(example_input3) == 0

@pytest.fixture
def example_input4():
    return fileinput.input(F_NAME + '.test.4')

def test_answer4(example_input4):
    assert answer(example_input4) == 0

@pytest.fixture
def example_input5():
    return fileinput.input(F_NAME + '.test.5')

def test_answer5(example_input5):
    assert answer(example_input5) == 0

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

