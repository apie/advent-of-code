#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
from collections import Counter
from functools import cmp_to_key

CARD_ORDER = '23456789TJQKA'


def get_handtype(handstr):
#    print(handstr)
    hand = set(handstr)
    score = 0
    if len(hand) == 5:
#        print('high card')
        return 4
    elif len(hand) == 4:
#        print('one pair')
        return 5
    elif len(hand) == 3:
        c = Counter(handstr)
        if c.most_common(1)[0][1] == 3:
#            print('three of a kind')
            return 7
#       print('two pair')
        return 6
    elif len(hand) == 2:
        c = Counter(handstr)
        if c.most_common(1)[0][1] == 4:
#            print('four of a kind')
            return 9
#        print('full house')
        return 8
    elif len(hand) == 1:
#        print('five of a kind')
        return 10
    1/0

def cardsort(hand_a, hand_b):
    a_type, b_type = get_handtype(hand_a), get_handtype(hand_b)
#    print(a_type, b_type)
    if a_type > b_type: return 1
    if a_type < b_type: return -1
#    print(hand_a, hand_b)
    for a, b in zip(hand_a, hand_b):
#        print(a, CARD_ORDER.index(a))
#        print(b, CARD_ORDER.index(b))
        if CARD_ORDER.index(a) > CARD_ORDER.index(b): return 1
        if CARD_ORDER.index(a) < CARD_ORDER.index(b): return -1

def answer(lines):
    bids = {}
    hands = []
    for line in map(str.strip, lines):
#        print(line)
        handstr, bid = line.split()
        bids[handstr] = int(bid)
        hands.append(handstr)
    hands.sort(key=cmp_to_key(cardsort))
    import pprint
#    pprint.pprint(hands)
#    print(bids)
    answer = 0
    for i, hand in enumerate(hands, start=1):
        answer += bids[hand] * i
        print(bids[hand],'*', i)
    return answer


@pytest.mark.parametrize('testfileno, expected', [
    (1, 6440),
    (2, 205),
])
def test_answer_testfiles(testfileno, expected):
    print()
    assert answer(fileinput.input(f"{F_NAME}.test.{testfileno}")) == expected

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

