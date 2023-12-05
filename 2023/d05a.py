#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
import re
from collections import defaultdict

def parse_map(line_iter):
    parsed_map = []
    line = next(line_iter)
    while line:
        dest_range_start, source_range_start, range_length = map(int, line.split())
        print(dest_range_start, source_range_start, range_length)
        parsed_map.append((dest_range_start, source_range_start, range_length))
        try:
            line = next(line_iter)
        except StopIteration:
            line = ''
    return parsed_map

def answer(lines):
    linez = map(str.strip, lines)
    maps = []
    while True:
        try:
            line = next(linez)
        except StopIteration:
            break
        print(line)
        if re.match(r'^seeds:', line):
            seeds = set(map(int, re.findall(r'\d+', line)))
            print(seeds)
            continue
        if re.match(r'.*map:$', line):
            parsed_map = parse_map(linez)
            print('map:', len(maps))
            maps.append(parsed_map)
            continue
    print()
    answer = 99999999999999999
    for seed in seeds:
        n = seed
        print(f'{n=}')
        for i, m in enumerate(maps):
            if i == 6:
                print(f'{i=} {n=}')
            found = False
            for ma in m:
                dest_range_start, source_range_start, range_length = ma
                if n >= source_range_start and n < source_range_start + range_length:
                    if not found:
                        n = n - source_range_start + dest_range_start
                        found = True
#                print(n)
        answer = min(n, answer)
    print(answer)
    return answer


@pytest.mark.parametrize('testfileno, expected', [
    (1, 35),
])
def test_answer_testfiles(testfileno, expected):
    print()
    assert answer(fileinput.input(f"{F_NAME}.test.{testfileno}")) == expected

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

