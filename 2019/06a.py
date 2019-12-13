#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath

class Tree():
    def __init__(self, data, level=0):
        self.left = []
        self.right = []
        self.data = data
        self.level = level
    def add(self, data):
        if not self.left:
            self.left = Tree(data, self.level+1)
        elif not self.right:
            self.right = Tree(data, self.level+1)
        else:
            raise
    def __repr__(self):
        return f"({self.left or ''}{self.data}{self.level}{self.right or ''})"
    def __iter__(self):
        yield self
        yield from self.left
        yield from self.right

def answer(in_lines):
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
            found = True
        elif top:
            for planet in top:
                if planet.data == orbited:
                    planet.add(orbits)
                    found = True
        if not found:
            lines.add(l)
    som = 0
    for planet in top:
        print(planet)
        som += planet.level
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

