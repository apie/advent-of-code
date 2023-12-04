#!/usr/bin/env python3
import pytest
import fileinput
from os.path import splitext, abspath
F_NAME = splitext(abspath(__file__))[0][:-1]

def answer(lines):
    answer = 0
    for line in map(str.strip, lines):
        print(line)
        winning_numbers = set(line.split(':')[1].split('|')[0].split())
        your_numbers = set(line.split(':')[1].split('|')[1].split())
        print(f'{winning_numbers=}')
        print(f'{your_numbers=}')
        number_of_winning = winning_numbers.intersection(your_numbers)
        print(f'{number_of_winning=}')
        if number_of_winning:
            score = 2**(len(number_of_winning)-1)
            answer += score
    return answer


@pytest.mark.parametrize('testfileno, expected', [
    (1, 13),
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

