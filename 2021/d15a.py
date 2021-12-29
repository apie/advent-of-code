#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
import networkx as nx


def answer(lines):
    #find paths trough the maze, starting at 0,0 (dont count in total) and ending at maxx,maxy
    #you can not move diagonally
    #return the total risk of the path with the lowest total
    lines = list(lines)
    maxy = len(lines)-1
    maxx = len(lines[0].strip())-1
    print()
    G = nx.DiGraph()
    # input is a map of risk levels
    for y, line in enumerate(map(str.strip, lines)):
        for x in range(len(line)):
            weight = int(line[x])
            edges = []
            # add all inward edges
            if x>0:    edges.append(((x-1,y  ), (x,y), weight)) #left ->
            if x<maxx: edges.append(((x+1,y  ), (x,y), weight)) #right <-
            if y>0:    edges.append(((x  ,y-1), (x,y), weight)) #top \/
            if y<maxy: edges.append(((x  ,y+1), (x,y), weight)) #bottom /\
            G.add_weighted_edges_from(edges)

    def print_graph():
        for y in range(maxy+1):
            for x in range(maxx+1):
                n = (x,y)
                if n[0] % (maxx+1) == 0:
                    print()
                try:
                    print(G[(n[0]-1, n[1])][n]['weight'], end='') #left
                except KeyError:
                    try:
                        print(G[(n[0], n[1]-1)][n]['weight'], end='') #top
                    except KeyError:
                        print('x', end='')
        print()
    def print_path(path):
        prevn = path[0] 
        for y in range(maxy+1):
            for x in range(maxx+1):
                n = (x,y)
                if n[0] % (maxx+1) == 0:
                    print()
                if n in path:
                    try:
                        w = int(G[prevn][n]['weight'])
                    except KeyError:
                        w = 'x'
                    print(w, end='')
                    prevn = n
                else:
                    print('.', end='')
        print()

    print_graph()
    startp = (0,0)
    endp = (maxx, maxy)
    sp = nx.shortest_path(G, startp, endp, 'weight')
#    return nx.shortest_path_length(G, startp, endp, 'weight')
    print_path(sp)
    return nx.path_weight(G, sp, 'weight')

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer_10x10(example_input):
    assert answer(example_input) == 40

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')


