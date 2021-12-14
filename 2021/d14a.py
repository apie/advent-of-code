#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
from collections import Counter

F_NAME = splitext(abspath(__file__))[0][:-1]
STEPS = 10

def answer(lines):
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
        return template, rules
                

    def apply_rules(rules, polymer):
        result = polymer
        for i in reversed(range(len(polymer))):
            if i == 0:
                continue
            pair = polymer[i-1] + polymer[i]
            extra = rules.get(pair)
            if extra:
                result.insert(i, extra)
            print(f'{pair=} {extra=}')
        return result

    template, rules = parse_input(lines)
    polymer = list(template)

    #apply the rules to each pair
    #repeat this for STEPS times
    for x in range(STEPS):
        polymer = apply_rules(rules, polymer)

    print(len(polymer))
    c = Counter(polymer)
    common_elements = c.most_common()
    #find most common elements in polymer
    #find least common elements in polymer
    return common_elements[0][1] - common_elements[-1][1]

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    assert answer(example_input) == 1588

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)

