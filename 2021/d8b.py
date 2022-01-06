#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
'''
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
'''

N_SEGMENTS_DIGIT = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}

def get_mapping(patterns):
    pattern_set = {''.join(sorted(pattern)) for pattern in patterns}
    inv_mapping = {}
    wiring = {}
    def found(d, p):
        print(f'found {d}')
        inv_mapping[d] = p
        pattern_set.remove(p)
    # Find 1, 4, 7, 8
    for p in list(pattern_set):
        if d := N_SEGMENTS_DIGIT.get(len(p)):
            found(d, p)
    wiring['a'] = set(inv_mapping[7]).difference(inv_mapping[1]).pop()
    # Find 0, 6, 9
    for p in list(pattern_set):
        if len(p) != 6:
            continue
        # Must be 0, 6 or 9
        # If it doesnt have all the segments of 1, it is 6
        if not set(inv_mapping[1]).issubset(set(p)):
            found(6, p)
            wiring['c'] = set(inv_mapping[8]).difference(inv_mapping[6]).pop()
        # Must be 0 or 9
        # If 4 is contained within p it is 9 and not 0
        elif set(inv_mapping[4]).issubset(set(p)):
            found(9, p)
            wiring['e'] = set(inv_mapping[8]).difference(inv_mapping[9]).pop()
        else:
            found(0, p)
            wiring['d'] = set(inv_mapping[8]).difference(inv_mapping[0]).pop()
    # Find 5
    for p in list(pattern_set):
        # If p is contained within 6 it is 5
        if set(p).issubset(set(inv_mapping[6])):
            found(5, p)
            break
    # Find 3
    for p in list(pattern_set):
        # If p is contained within 9 it is 3 and not 2
        if set(p).issubset(set(inv_mapping[9])):
            found(3, p)
            wiring['b'] = set(inv_mapping[9]).difference(inv_mapping[3]).pop()
            break
    # Find 2. It is the last one left
    assert len(pattern_set) == 1
    assert 2 not in inv_mapping
    found(2, list(pattern_set)[0])
    # -- Mapping complete
    # 2 is the only one without f
    wiring['f'] = set(inv_mapping[8]).difference(inv_mapping[2]).difference(wiring['b']).pop()
    assert len(wiring) == 6
    # g remains. Remove all existing wirings and find the one that remains.
    possible = set(list('abcdefg'))
    for w in wiring.keys():
        possible = possible.difference(wiring[w])
    wiring['g'] = possible.pop()
    # -- Wiring complete
    print(f'{inv_mapping=}')
    print(f'{inv_mapping.keys()=}')
    print(f'{sorted(wiring.keys())=}')
    print(f'{wiring=}')
    assert len(pattern_set) == 0, pattern_set
    assert len(inv_mapping) == 10, inv_mapping
    assert len(wiring) == 7, wiring

    # Invert mapping
    return {v: k for k, v in inv_mapping.items()}

def get_digit(digits, mapping):
    print(digits)
    retval = 0
    for d in digits:
        md = mapping[''.join(sorted(d))]
        retval = retval*10 + md
    print(retval)
    return retval

def answer(lines):
    tot = 0
    for line in map(str.strip, lines):
        print(line)
        signal_patterns, output_value = line.split(' | ')
        mapping = get_mapping(signal_patterns.split())
        tot += get_digit(output_value.split(), mapping)
    return tot

@pytest.fixture
def example_input1():
    # Cast to list since we use it in multiple tests (we need to iterate it multiple times)
    return list(fileinput.input(F_NAME + '.test.1'))

def test_answer1_map(example_input1):
    line = next(iter(example_input1))
    signal_patterns, output_value = line.split(' | ')
    mapping = get_mapping(signal_patterns.split())
    testm = {
        ''.join(sorted('acedgfb')): 8,
        ''.join(sorted('cdfbe')): 5,
        ''.join(sorted('gcdfa')): 2,
        ''.join(sorted('fbcad')): 3,
        ''.join(sorted('dab')): 7,
        ''.join(sorted('cefabd')): 9,
        ''.join(sorted('cdfgeb')): 6,
        ''.join(sorted('eafb')): 4,
        ''.join(sorted('cagedb')): 0,
        ''.join(sorted('ab')): 1,
    }
    for k, v in testm.items():
        assert v == mapping[k]

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

