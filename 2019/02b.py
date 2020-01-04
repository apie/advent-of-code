#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
from intcodecomputer import IntCodeComputer

def find_noun_verb(in_line, output):
    for noun in range(100):
        for verb in range(100):
            instructions = list(map(int, in_line.strip().split(',')))
            instructions[1], instructions[2] = noun, verb
            in_line = ','.join(map(str, instructions))
            try:
                program_state = IntCodeComputer(in_line).run()
                out = program_state.split(',')[0]
                if out == str(output):
                    return noun, verb
            except Exception:
                pass

def answer(in_line):
    noun, verb = find_noun_verb(next(in_line), 19690720)
    return 100 * noun + verb


@pytest.mark.parametrize("inp, exp, noun, verb", [
    ('1,1,1,4,99,5,6,0,99', 30, 0, 0),
    ('2,0,0,0,99', 2, 1, 0),
])
def test_find_noun_verb(inp, exp, noun, verb):
    assert find_noun_verb(inp, exp) == (noun, verb)


if __name__ == '__main__':
    print(answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input')))

