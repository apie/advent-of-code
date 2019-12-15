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
    you_orbit = san_orbits = None
    while lines:
        l = lines.pop()
        if not l.strip():
            continue
        orbited, orbits = l.strip().split(')')
        found = False
        if orbits == 'YOU' and not you_orbit:
            print(f'{orbits} orbit {orbited}')
            you_orbit = orbited
        if orbits == 'SAN' and not san_orbits:
            print(f'{orbits} orbits {orbited}')
            san_orbits = orbited
        if not top and orbited == 'COM':
            top = Tree(orbited)
            top.add(orbits)
            lut[orbited] = top
            found = True
        elif top:
            if orbited in lut:
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
    you = lut[you_orbit].parents
    steps_to_you = len(you)
    print(steps_to_you)
    santa = lut[san_orbits].parents
    steps_to_santa = len(santa)
    print(steps_to_santa)
    lca = you & santa
    steps_to_lca = len(lca)-1
    steps_between_you_and_santa = steps_to_you - steps_to_lca + steps_to_santa - steps_to_lca
    print(datetime.datetime.now()-start)
    print(steps_between_you_and_santa)
    return steps_between_you_and_santa

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
    K)YOU
    I)SAN
    '''

def test_answer(example_input):
    assert answer(iter(reversed(example_input.split('\n')))) == 4

if __name__ == '__main__':
    a = answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input'))
    assert a > 247
    print(a)

