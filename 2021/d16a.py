#!/usr/bin/env python3
import pytest
import sys
import fileinput
from os.path import splitext, abspath
from bitstring import BitStream
F_NAME = splitext(abspath(__file__))[0][:-1]
LITERAL_TYPE = 4

class Reader:

    def __init__(self, bs, level=0):
        self.bs = bs
        self.version_sum = 0
        self.level = level

    def read_packet(self):
        print('-'*self.level, end=' ')
        #read version and packet type_id
        version, packet_type_id = self.bs.readlist('2*uint:3')
        self.version_sum += version
        if packet_type_id == LITERAL_TYPE:
            lv = 0
            not_last_group = True
            while not_last_group:
                lv <<= 4
                not_last_group, group = self.bs.readlist('bool, uint:4')
                lv += group
            print(f'LIT {version=} {packet_type_id=} {lv=}')
        else:
            print('OPT', end=' ')
            length_type_id = self.bs.read('bool')
            if not length_type_id:
                n_bits_subpackets = self.bs.read('uint:15')
                print(f'{version=} {packet_type_id=} {n_bits_subpackets=}')
                p = Reader(self.bs, level=self.level+1)
                end = p.bs.pos + n_bits_subpackets
                #read n_bits of subpackets
                while p.bs.pos < end:
                    p.read_packet()
            else:
                n_subpackets = self.bs.read('uint:11')
                print(f'{version=} {packet_type_id=} {n_subpackets=}')
                p = Reader(self.bs, level=self.level+1)
                #read n subpackets
                for i in range(n_subpackets):
                    p.read_packet()
            self.version_sum += p.version_sum

def answer(lines):
    print()
    line = next(map(str.strip, lines))
    bs = BitStream('0x'+line)
    print(f'{bs.hex=}')
    print(f'{bs.bin=}')
    p = Reader(bs)
    p.read_packet()
    version_sum = p.version_sum
    print(f'{version_sum=}')
    if p.bs.pos != p.bs.len:
        rest = p.bs.read(p.bs.len - p.bs.pos)
        print(f'---REST: {rest}')
        assert rest.all(0)
    return version_sum

def test_answer():
    assert answer(['D2FE28']) == 6
def test_answer_with_op():
    assert answer(['38006F45291200']) == 9
def test_answer_with_op2():
    assert answer(['EE00D40C823060']) == 14
def test_answer_with_op3():
    assert answer(['8A004A801A8002F478']) == 16
def test_answer_with_op4():
    assert answer(['620080001611562C8802118E34']) == 12
def test_answer_with_op5():
    assert answer(['C0015000016115A2E0802F182340']) == 23
def test_answer_with_op6():
    assert answer(['A0016C880162017C3686B18A3D4780']) == 31

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    filename = fileinput.input(F_NAME + '.input')
    ans = answer(filename)
    print('Answer:', ans)
    duration = timeit.default_timer()-start
    print(f'Execution time: {duration:.3f} s')

