#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath

class IntCodeComputer:
    def __init__(self, in_line):
        self.instructions = list(map(int, in_line.strip().split(',')))
    def run(self):
        for pos in range(0, len(self.instructions)+1, 4):
            opcode = self.instructions[pos]
            if opcode == 1:
                operation = lambda x1, x2: x1 + x2
            elif opcode == 2:
                operation = lambda x1, x2: x1 * x2
            elif opcode == 99:
                break
            else:
                raise Exception(f'Unknown opcode {opcode}')
            op_pos_1, op_pos_2, result_pos = self.instructions[pos+1], self.instructions[pos+2], self.instructions[pos+3]
            self.instructions[result_pos] = operation(self.instructions[op_pos_1], self.instructions[op_pos_2])
        return ','.join(map(str, self.instructions))

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


@pytest.mark.parametrize("inp, exp", [
    ('1,9,10,3,2,3,11,0,99,30,40,50', '3500,9,10,70,2,3,11,0,99,30,40,50'),
    ('1,0,0,0,99', '2,0,0,0,99'),
    ('2,3,0,3,99', '2,3,0,6,99'),
    ('2,4,4,5,99,0', '2,4,4,5,99,9801'),
    ('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99'),
])
def test_run_program(inp, exp):
    assert IntCodeComputer(inp).run() == exp

@pytest.mark.parametrize("inp, exp, noun, verb", [
    ('1,1,1,4,99,5,6,0,99', 30, 0, 0),
    ('2,0,0,0,99', 2, 1, 0),
])
def test_find_noun_verb(inp, exp, noun, verb):
    assert find_noun_verb(inp, exp) == (noun, verb)


if __name__ == '__main__':
    print(answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input')))

