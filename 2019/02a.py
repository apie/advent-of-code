#!/usr/bin/env python3
import sys
import fileinput
from os.path import splitext, abspath
from intcodecomputer import IntCodeComputer


def answer(in_line):
    instructions = list(map(int, next(in_line).strip().split(',')))
    instructions[1], instructions[2] = 12, 2
    in_line = ','.join(map(str, instructions))
    program_state = IntCodeComputer(in_line).run()
    return program_state.split(',')[0]


if __name__ == '__main__':
    print(answer(fileinput.input(sys.argv[1:] or splitext(abspath(__file__))[0][:-1] + '.input')))

