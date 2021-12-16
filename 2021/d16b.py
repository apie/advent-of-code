#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
from bitstring import BitStream
F_NAME = splitext(abspath(__file__))[0][:-1]

LITERAL_TYPE = 4
OPS = {
    0: int.__add__,
    1: int.__mul__,
    2: min,
    3: max,
    5: int.__gt__,
    6: int.__lt__,
    7: int.__eq__,
}

class Reader:

    def __init__(self, bs, level=0):
        self.bs = bs
        self.level = level

    def read_packet(self):
        print('-'*self.level, end=' ')
        #read version and packet type_id
        version, packet_type_id = self.bs.readlist('2*uint:3')
        if packet_type_id == LITERAL_TYPE:
            literal_value = 0
            not_last_group = True
            while not_last_group:
                literal_value <<= 4
                not_last_group, group = self.bs.readlist('bool, uint:4')
                literal_value += group
            print(f'LIT {literal_value}')
            return literal_value
        else:
            op = OPS[packet_type_id]
            print(f'OPT {op.__name__}')
            result = None
            length_type_id = self.bs.read('bool')
            if not length_type_id:
                n_bits_subpackets = self.bs.read('uint:15')
                p = Reader(self.bs, level=self.level+1)
                end = p.bs.pos + n_bits_subpackets
                #read n_bits of subpackets
                while p.bs.pos < end:
                    r = p.read_packet()
                    result = r if result is None else op(result, r)
            else:
                n_subpackets = self.bs.read('uint:11')
                p = Reader(self.bs, level=self.level+1)
                #read n subpackets
                for i in range(n_subpackets):
                    r = p.read_packet()
                    result = r if result is None else op(result, r)
            print('-'*self.level, f'{op.__name__} {result=}')
            return result

def answer(lines):
    print()
    line = next(map(str.strip, lines))
    bs = BitStream('0x'+line)
    print(f'{bs.hex=}')
    print(f'{bs.bin=}')
    p = Reader(bs)
    result = p.read_packet()
    if p.bs.pos != p.bs.len:
        rest = p.bs.read(p.bs.len - p.bs.pos)
        print(f'---REST: {rest.bin}')
        assert rest.all(0)
    return result

def test_answer_product_6_0():
    assert answer(['04005AC33800']) == 0
def test_answer_sum_1_2():
    assert answer(['C200B40A82']) == 3
def test_answer_product_6_9():
    assert answer(['04005AC33890']) == 54
def test_answer_min_7_8_9():
    assert answer(['880086C3E88112']) == 7
def test_answer_max_7_8_9():
    assert answer(['CE00C43D881120']) == 9
def test_answer_lt_5_15():
    assert answer(['D8005AC2A8F0']) == 1
def test_answer_gt_5_15():
    assert answer(['F600BC2D8F']) == 0
def test_answer_eq_5_15():
    assert answer(['9C005AC2F8F0']) == 0
def test_answer_sum_1_3_eq_product_2_2():
    assert answer(['9C0141080250320F1802104A08']) == 1
    

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

