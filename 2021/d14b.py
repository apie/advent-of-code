#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
from collections import Counter
from collections import defaultdict

F_NAME = splitext(abspath(__file__))[0][:-1]

def answer(lines, STEPS):
    def parse_input(lines):
        template = None
        rules = dict()
        for line in map(str.strip, lines):
#            print(line)
            if not line:
                continue
            if '->' in line:
                p, res = line.split(' -> ')
                rules[p] = res
                continue
            if not template:
                template = line
        return list(template), rules
                
    pair_count = defaultdict(int)
    def apply_rules(rules):
        for pair, v in list(pair_count.items()):
            if v <= 0:
                continue
            extra = rules.get(pair)
            if extra:
                new_pair1 = pair[0] + extra
                new_pair2 = extra + pair[1]
                pair_count[pair] -= v
                pair_count[new_pair1] += v
                pair_count[new_pair2] += v
                element_count[extra] += v
#                print(f'{pair=} {extra=} {new_pair1=} {new_pair2=}')

    template, rules = parse_input(lines)
    element_count = defaultdict(int)
    for c in template:
        element_count[c] += 1
    # add template to pair_count
    for i in reversed(range(len(template))):
        if i == 0:
            continue
        pair_count[template[i-1] + template[i]] += 1

    lenp = sum(c for c in element_count.values()) #lenght of polymer
#    print(lenp)
    #apply the rules to each pair
    #repeat this for STEPS times
    for x in range(STEPS):
        apply_rules(rules)

    c = Counter(element_count)
    common_elements = c.most_common()
    #find most common elements in polymer
    #find least common elements in polymer
    return common_elements[0][1] - common_elements[-1][1]

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input, 10) == 1588

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename, 40)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

