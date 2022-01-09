#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = 'd8'
#implement day8 using bits

def find_ones(d):
    '''count number of ones in binary number'''
    ones = 0
    while d > 0:
        ones += d & 1
        d >>= 1
    return ones

# Assign each segment a 'wire'.
lut = {
    'a':0b0000001,
    'b':0b0000010,
    'c':0b0000100,
    'd':0b0001000,
    'e':0b0010000,
    'f':0b0100000,
    'g':0b1000000,
}

def solve_line(line):
    def solve_output_val(output_values):
        '''Look up each output val in binary repr in the mapping and add them together shifting each digit to the left.'''
        output = 0
        for o in output_values:
            b_val = sum(lut[c] for c in o)
            for k,v in mapping.items():
                if v == b_val:
                    output = output*10 + k
                    break
            else:
                raise Exception(b_val, 'not found')
        return output

    def found(digit, bit_pattern):
        mapping[digit] = bit_pattern
        bpatterns.remove(bit_pattern)

    signal_pattern, output_value = line.split(' | ')
    # Convert letter string to binary pattern
    bpatterns = {
        sum(lut[c] for c in p)
        for p in signal_pattern.split()
    }

    ## Search for each digit and if found, remove it from bpatterns and add the digit to the mapping.
    ######################################
    mapping = {}

    # 1,4,7,8 all have a unique count of segments. Find them.
    for bp in list(bpatterns):
        if find_ones(bp) == 2:
            found(1, bp)
        elif find_ones(bp) == 4:
            found(4, bp)
        elif find_ones(bp) == 3:
            found(7, bp)
        elif find_ones(bp) == 7:
            found(8, bp)

    # Find 0, 6, 9. All have 6 segments
    for bp in list(bpatterns):
        if find_ones(bp) != 6:
            continue
        #is 4 contained within p, then it is 9
        if mapping[4] & bp >= mapping[4]:
            found(9, bp)
        #is 1 contained within p, then it is 0
        elif mapping[1] & bp >= mapping[1]:
            found(0, bp)
        else: # 6 is left
            found(6, bp)

    #is p contained within 6, then it is 5
    for bp in bpatterns:
        if mapping[6] & bp >= bp:
            found(5, bp)
            break

    #is p contained within 9, and it is not 8 or 5, then it is 3
    for bp in bpatterns:
        if mapping[9] & bp >= bp:
            found(3, bp)
            break

    assert len(bpatterns) == 1, bpatterns
    #what is left is 2
    for bp in bpatterns:
        found(2, bp)
        break

    assert len(bpatterns) == 0, bpatterns
    return solve_output_val(output_value.split())


def answer(lines):
    return sum(solve_line(line) for line in map(str.strip, lines))


@pytest.fixture
def example_input1():
    return fileinput.input(F_NAME + '.test.1')

def test_answer1(example_input1):
    assert answer(example_input1) == 5353

@pytest.fixture
def example_input():
     return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
     assert answer(example_input) == 61229

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

