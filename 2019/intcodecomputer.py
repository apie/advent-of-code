import pytest


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


@pytest.mark.parametrize("inp, exp", [
    ('1,9,10,3,2,3,11,0,99,30,40,50', '3500,9,10,70,2,3,11,0,99,30,40,50'),
    ('1,0,0,0,99', '2,0,0,0,99'),
    ('2,3,0,3,99', '2,3,0,6,99'),
    ('2,4,4,5,99,0', '2,4,4,5,99,9801'),
    ('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99'),
])
def test_run_program(inp, exp):
    assert IntCodeComputer(inp).run() == exp
