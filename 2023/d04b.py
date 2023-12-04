#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
from collections import defaultdict

def answer(lines):
    cards = defaultdict(int)
    winmap = defaultdict(set)
    # parse input. make a winmap
    for line in map(str.strip, lines):
        cardno = int(line.split(':')[0].split()[1])
        winning_numbers = set(line.split(':')[1].split('|')[0].split())
        your_numbers = set(line.split(':')[1].split('|')[1].split())
        number_of_winning = winning_numbers.intersection(your_numbers)
        cards[cardno] += 1
        if number_of_winning:
            for i in range(1, len(number_of_winning)+1):
                winmap[cardno].add(cardno+i)

    # increase the count of each card based on the winmap
    for k, v in winmap.items():
        for nextc in v:
            cards[nextc] += cards[k]

    return sum(cards.values())


@pytest.mark.parametrize('testfileno, expected', [
    (1, 30),
])
def test_answer_testfiles(testfileno, expected):
    assert answer(fileinput.input(f"{F_NAME}.test.{testfileno}")) == expected

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

