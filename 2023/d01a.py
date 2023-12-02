#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]
import re

def answer(lines):
    answer = 0
    for line in map(str.strip, lines):
        print(line)
        digits_line = re.sub(r'\D', '', line)
        calibration_values = digits_line[0] + digits_line[-1]
        print(calibration_values)
        answer += int(calibration_values)
    return answer

@pytest.mark.parametrize('testfileno, expected', [
    (1, 142),
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

