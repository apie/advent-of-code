#!/usr/bin/env python3
import datetime
import pytest
import sys
import fileinput
from os.path import splitext, abspath

class Tree():
    def __init__(self, data, level=0, parents=None):
        if not parents:
            parents = set()
        self.left = []
        self.right = []
        self.data = data
        self.level = level
        self.parents = parents
    def add(self, data):
        parents = set(self.parents)
        parents.add(self.data)
        t = Tree(data, self.level+1, parents)
        if not self.left:
            self.left = t
        elif not self.right:
            self.right = t
        else:
            raise
    def __repr__(self):
        return f"({self.left or ''}{self.data}{self.level}[{self.parents}]{self.right or ''})"
    def __iter__(self):
        yield self
        yield from self.left
        yield from self.right

def answer(in_lines):
    start = datetime.datetime.now()
    lut = dict()
    print('')
    top = None
    lines = set(in_lines)
    while lines:
        l = lines.pop()
        if not l.strip():
            continue
        orbited, orbits = l.strip().split(')')
        found = False
        if not top and orbited == 'COM':
            top = Tree(orbited)
            top.add(orbits)
            lut[orbited] = top
            found = True
        elif top:
            if orbited in lut:
                print('found')
                lut[orbited].add(orbits)
                found = True
            elif True:
                for planet in top:
                    if planet.data == orbited:
                        planet.add(orbits)
                        lut[orbited] = planet
                        found = True
        if not found:
            lines.add(l)
    print(datetime.datetime.now()-start)
    som = 0
    for planet in top:
        print(planet)
        som += len(planet.parents)
    print(datetime.datetime.now()-start)
    return som

@pytest.fixture
def example_input():
    return '''
    COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L
    '''

def test_answer(example_input):
    assert answer(iter(example_input.split('\n'))) == 42
    assert answer(iter(reversed(example_input.split('\n')))) == 42

if __name__ == '__main__':
    print(answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input')))

