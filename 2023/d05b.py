#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
import re
from functools import lru_cache

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
    return sorted(parsed_map)

def parse_input(lines):
    linez = map(str.strip, lines)
    maps = []
    while True:
        try:
            line = next(linez)
        except StopIteration:
            break
        print(line)
        if re.match(r'^seeds:', line):
            seeds = list(map(int, re.findall(r'\d+', line)))
            print(seeds)
            continue
        if re.match(r'.*map:$', line):
            parsed_map = parse_map(linez)
            print('map:', len(maps))
            maps.append(parsed_map)
            continue
    return seeds, maps

def answer(lines):
    seeds, maps = parse_input(lines)
    print()
    answer = 99999999999999999

    print('location we are looking for must be lower than lower bound of location numbers in the input:')
    print(maps[-1][0][0])
    upper_bound = maps[-1][0][0]
    print('search for a humidity based on that upper bound')
    humiditys=maps[-2]
    humidityfound=False
    for humidity in humiditys:
        if humidity[0] <= upper_bound <= humidity[0] + humidity[2]:
            humidityfound=humidity
            print(humidity)
    if humidityfound:
        upper_bound = upper_bound - humidityfound[0] + humidityfound[1]
        print('new upper bound:', upper_bound)
    else:
        print('humidity not found, use same')
            
    print('search for a temp based on that upper bound')
    temps=maps[-3]
    tempfound=False
    for temp in temps:
        if temp[0] <= upper_bound <= temp[0] + temp[2]:
            tempfound=temp
            print(temp)
    if tempfound:
        upper_bound = upper_bound - tempfound[0] + tempfound[1]
        print('new upper bound:', upper_bound)
    else:
        print('temp not found, use same')
            
    print('search for a light based on that upper bound')
    lights=maps[-4]
    lightfound=False
    for light in lights:
        if light[0] <= upper_bound <= light[0] + light[2]:
            lightfound=light
            print(light)
    if lightfound:
        upper_bound = upper_bound - lightfound[0] + lightfound[1]
        print('new upper bound:', upper_bound)
    else:
        print('lightfound not found, use same')
            
    print('search for a water based on that upper bound')
    water=maps[-5]
    waterfound=False
    for w in water:
        if w[0] <= upper_bound <= w[0] + w[2]:
            waterfound=w
            print(w)
    if waterfound:
        upper_bound = upper_bound - waterfound[0] + waterfound[1]
        print('new upper bound:', upper_bound)
    else:
        print('waterfound not found, use same')

            
    print('search for a fertilizer based on that upper bound')
    fertilizer=maps[-6]
    fertilizerfound=False
    for w in fertilizer:
        if w[0] <= upper_bound <= w[0] + w[2]:
            fertilizerfound=w
            print(w)
    if fertilizerfound:
        upper_bound = upper_bound - fertilizerfound[0] + fertilizerfound[1]
        print('new upper bound:', upper_bound)
    else:
        print('fertilizerfound not found, use same')

            
    print('search for a soil based on that upper bound')
    soil=maps[-7]
    soilfound=False
    for w in soil:
        if w[0] <= upper_bound <= w[0] + w[2]:
            soilfound=w
            print(w)
    if soilfound:
        upper_bound = upper_bound - soilfound[0] + soilfound[1]
        print('new upper bound:', upper_bound)
    else:
        print('soilfound not found, use same')

            


    upper_bound += 1

    while seeds:
        start = seeds.pop(0)
        seed_range = (start, start + seeds.pop(0))
#        print(f'{seed_range=}')
#        breakpoint()
        for n in range(*seed_range):
            if n > upper_bound:
                continue

            @lru_cache(maxsize=None)
            def getmin(n):
                for i, m in enumerate(maps):
#                    if i == 6:
#                        print(f'{seed_range=} {i=} {n=} {answer=}')
                    found = False
                    ma = m[0]
                    if True:
#                    for ma in m:
                        if found:
                            break
                        dest_range_start, source_range_start, range_length = ma
                        if n >= source_range_start and n < source_range_start + range_length:
                            if not found:
                                n = n - source_range_start + dest_range_start
                                found = True
        #                print(n)
                return n

            answer = min(getmin(n), answer)

    print(answer)
    return answer


@pytest.mark.parametrize('testfileno, expected', [
    (1, 46),
])
def test_answer_testfiles(testfileno, expected):
    print()
    assert answer(fileinput.input(f"{F_NAME}.test.{testfileno}")) == expected

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    assert ans < 1617282249
    assert ans < 403695602
    assert ans < 219538664
    assert ans != 629551616
    assert ans != 105822591
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

