#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath

def add(x1, x2):
    return x1 + x2
def mul(x1, x2):
    return x1 * x2

def run_program(in_lines):
    ll = [l for l in in_lines]
    assert len(ll) == 1, ll
    instructions = list(map(int, ll[0].strip().split(',')))
    pos = 0
    while True:
        opcode = instructions[pos]
        if opcode == 1:
            operation = add
        elif opcode == 2:
            operation = mul
        elif opcode == 99:
            break
        instructions[instructions[pos+3]] = operation(instructions[instructions[pos+1]], instructions[instructions[pos+2]])
        pos += 4
    return ','.join(map(str, instructions))

def answer(in_lines):
    ll = [l for l in in_lines]
    instructions = list(map(int, ll[0].strip().split(',')))
    instructions[1], instructions[2] = 12, 2
    in_lines = [','.join(map(str, instructions))]
    program_state = run_program(in_lines)
    return program_state.split(',')[0]

@pytest.mark.parametrize("inp, exp", [
    ('1,9,10,3,2,3,11,0,99,30,40,50', '3500,9,10,70,2,3,11,0,99,30,40,50'),
    ('1,0,0,0,99', '2,0,0,0,99'),
    ('2,3,0,3,99', '2,3,0,6,99'),
    ('2,4,4,5,99,0', '2,4,4,5,99,9801'),
    ('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99'),
])
def test_run_program(inp, exp):
    assert run_program(iter(inp.split('\n'))) == exp


if __name__ == '__main__':
    print(answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input')))


