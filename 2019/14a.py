#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
from collections import defaultdict


def answer(l):
    '''How much ORE is required to produce 1 FUEL?'''
    return NanoFactory(l).lookup(1, 'FUEL')

class NanoFactory:
    def __init__(self, in_lines):
        self.chemical_book = dict()
        self.inventory = defaultdict(int)
        self._parse_input(in_lines)

    def _parse_input(self, in_lines):
        for l in in_lines:
            if not l.strip():
                continue
            source, dest = l.strip().split('=>')
            n_dest, name_dest = dest.split()
            assert name_dest not in self.chemical_book, "Already in the book"
            self.chemical_book[name_dest] = (int(n_dest), source)

    def lookup(self, amount, chemical):
        print(f'Looking up {amount} {chemical}')
        self.inventory[chemical] -= amount
        if chemical == 'ORE':
            return
        n_dest, sources = self.chemical_book[chemical]
        while self.inventory[chemical] < 0:
            for source in sources.split(','):
                source_n, source_name = source.split()
                self.lookup(int(source_n), source_name)
            self.inventory[chemical] += int(n_dest)
        return -self.inventory['ORE']

@pytest.fixture
def example_input1():
    return '''10 ORE => 10 A
    1 ORE => 1 B
    7 A, 1 B => 1 C
    7 A, 1 C => 1 D
    7 A, 1 D => 1 E
    7 A, 1 E => 1 FUEL'''

@pytest.fixture
def example_input2():
    return '''9 ORE => 2 A
    8 ORE => 3 B
    7 ORE => 5 C
    3 A, 4 B => 1 AB
    5 B, 7 C => 1 BC
    4 C, 1 A => 1 CA
    2 AB, 3 BC, 4 CA => 1 FUEL'''

def test_answer1(example_input1):
    assert answer(iter(example_input1.split('\n'))) == 31
def test_answer2(example_input2):
    assert answer(iter(example_input2.split('\n'))) == 165

if __name__ == '__main__':
    print(answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input')))
