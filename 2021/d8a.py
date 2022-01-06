#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

N_SEGMENTS_DIGIT = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}
def count_digits_with_unique_number_of_segments(digits):
    print(digits)
    retval =  sum(len(d) in N_SEGMENTS_DIGIT for d in digits)
    print(retval)
    return retval

def answer(lines):
    tot = 0
    for line in map(str.strip, lines):
        print(line)
        signal_patterns, output_value = line.split(' | ')
        tot += count_digits_with_unique_number_of_segments(output_value.split())
    return tot

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 26

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

