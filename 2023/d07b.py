#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
from collections import Counter
from functools import cmp_to_key, lru_cache

CARD_ORDER = 'J23456789TQKA'


@lru_cache(maxsize=None)
def get_handtype(handstr):
    # calculate type of hand and return a ranking, so we can sort on it
    hand = set(handstr)
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
#        print('two pair')
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

def upgrade_hand(hand):
    # Replace all the Js in the hand with another card and pick the combination with the highest rank
    upgraded = get_handtype(hand)
    if 'J' in hand:
#        print('try upgrade hand', hand)
        for c in CARD_ORDER:
            ar = hand.replace('J', c)
            upgraded = max(upgraded, get_handtype(ar))
    return upgraded

def cardsort(hand_a, hand_b):
    # try to upgrade and then compare types
    a_type, b_type = upgrade_hand(hand_a), upgrade_hand(hand_b)
    if a_type > b_type: return 1
    if a_type < b_type: return -1
    # if same type, compare each card
    for a, b in zip(hand_a, hand_b):
        if CARD_ORDER.index(a) > CARD_ORDER.index(b): return 1
        if CARD_ORDER.index(a) < CARD_ORDER.index(b): return -1

def answer(lines):
    bids = {}
    hands = []
    for line in map(str.strip, lines):
        handstr, bid = line.split()
        bids[handstr] = int(bid)
        hands.append(handstr)
    hands.sort(key=cmp_to_key(cardsort))
    return sum(
        bids[hand] * i
        for i, hand in enumerate(hands, start=1)
    )


@pytest.mark.parametrize('testfileno, expected', [
    (1, 5905),
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

