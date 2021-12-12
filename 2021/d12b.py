#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
from collections import Counter
import networkx as nx

def answer(lines):
    print()
    def parse_input(lines):
        G = nx.Graph()
        for line in map(str.strip, lines):
#            print(line)
            p, c = line.split('-')
            G.add_edge(p, c)
        return G

    G = parse_input(lines)
#    print(f'{list(G.nodes)=}')
#    print(f'{list(G.edges)=}')
#    print(f'{list(G["start"])=}')

    routes = set()
    for p in G['start']:
        routes.add(('start', p))

    def getz():
        return len({r for r in routes if r[-1] == 'end'})

    def pr():
        for r in routes:
            if r[-1] != 'end':
                continue
            print(','.join(r))

    pr()
    size_incr = True
    while size_incr:
        prevsize = len(routes)
        newroutes = set()
        for r in routes:
            if r[-1] == 'end':
                continue #route complete
            for p in G[r[-1]]:
                if r+(p,) in routes or r+(p,) in newroutes:
                    continue # exists already
                if p == 'start':
                    continue # dont go back to start
                if 'end' in r:
                    continue

                if p.islower() and p != 'end':
                    if sum(1 for c in r if c==p) > 1:
                        continue # dont go to small caves more than twice
                    if p in r:
                        small_caves = (c for c in r if c.islower() and c not in ('start', 'end'))
                        scc = Counter(small_caves)
                        small_cave_visited_more_than_once = any(c for k,c in scc.most_common(1) if c > 1)
                        if small_cave_visited_more_than_once:
                            continue # dont go to small caves more than once if someone has visited a cave twice

                newroutes.add(r+(p,))
        routes.update(newroutes)
        size = len(routes)
        size_incr = size > prevsize
    pr()
    size = getz()
    print('Size:', size)
    return size


@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')
@pytest.fixture
def example_input2():
    return fileinput.input(F_NAME + '.test.2')
@pytest.fixture
def example_input3():
    return fileinput.input(F_NAME + '.test.3')

def test_answer(example_input):
    assert answer(example_input) == 36
def test_answer2(example_input2):
    assert answer(example_input2) == 103
def test_answer3(example_input3):
    assert answer(example_input3) == 3509

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)

