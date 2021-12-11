#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

SCORING = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
OPENING = ('(','[','{','<')
OPEN_TO_CLOSE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

def answer(lines):
    scores = []
    incomplete_lines = set()
    for line in map(str.strip, lines):
        stack = []
        illegal_line = False
        for i, c in enumerate(line):
            if c in OPENING:
                stack.append(c)
            else:
                expected = OPEN_TO_CLOSE[stack.pop()]
                if c != expected:
                    illegal_line = True
                    break
        if not illegal_line and line not in incomplete_lines:
            score = 0
            addthis = ''.join(OPEN_TO_CLOSE[s] for s in reversed(stack))
            print(f'{line} Incomplete line. Complete by adding {addthis}')
            incomplete_lines.add(line)
            for c in addthis:
                score *= 5
                score += SCORING[c]
#            print(score)
            scores.append(score)
#    print(sorted(scores))
    middle_score = sorted(scores)[((len(scores))//2)]
    print(middle_score)
    return middle_score

@pytest.fixture
def example_input():
    return fileinput.input(F_NAME + '.test')

def test_answer(example_input):
    print('')
    assert answer(example_input) == 288957

if __name__ == '__main__':
    ans = answer(fileinput.input(F_NAME + '.input'))
    print(ans)

