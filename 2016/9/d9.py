#!/usr/bin/env python3
from collections import deque

p2 = True

def get_decompress_len(s: str) -> int:
#    print(s)
    q = deque(s)
    l = 0
    while q:
        c = q.popleft()
        if c == '(':
            instr = ''
            while c != ')':
                c = q.popleft()
                if c != ')':
                    instr += c
#            print('>INSTR:', instr)
            repr1 = int(instr.split('x')[0])
            repr2 = int(instr.split('x')[1])
#            print('>REPR1:', repr1)
#            print('>REPR2:', repr2)
            data = ''
            for _ in range(repr1):
#                if q and q[0] == '(':
#                    while q[0] != ')':
#                        q.popleft()
#                    q.popleft()
                if q:
                    data += q.popleft()
            repr = len(data)
            l += repr1 * repr2
#            print('data', data)
            continue
#        print(c)
        l += 1
#    print(f'>L = {l}')
#    print()
    return l

with open('d09.input') as f:
    line = f.readline()
if not p2:
    # ADVENT contains no markers and decompresses to itself with no changes, resulting in a decompressed length of 6.
    assert get_decompress_len('ADVENT') == 6
    # A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a decompressed length of 7.
    assert get_decompress_len('A(1x5)BC') == 7
    # (3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.
    assert get_decompress_len('(3x3)XYZ') == 9
    # A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a decompressed length of 11.
    assert get_decompress_len('A(2x2)BCD(2x2)EFG') == 11
    # (6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but because it's within a data section of another marker, it is not treated any differently from the A that comes after it. It has a decompressed length of 6.
    assert get_decompress_len('(6x1)(1x3)A') == 6
    # X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18), because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped and not processed further.
    assert get_decompress_len('X(8x2)(3x3)ABCY') == 18


    answer = get_decompress_len(line.strip())

# Part 2

def get_decompress_len_v2(s: str) -> int:
#    print(s)
    q = deque(s)
    l = 0
    while q:
        c = q.popleft()
        if c == '(':
            instr = ''
            while c != ')':
                c = q.popleft()
                if c != ')':
                    instr += c
#            print('>INSTR:', instr)
            repr1 = int(instr.split('x')[0])
            repr2 = int(instr.split('x')[1])
#            print('>REPR1:', repr1)
#            print('>REPR2:', repr2)
            data = ''
            for _ in range(repr1):
#                if q and q[0] == '(':
#                    while q[0] != ')':
#                        q.popleft()
#                    q.popleft()
                if q:
                    data += q.popleft()
            repr = len(data)
#            print('data', data)
            if '(' in data:
                processed_data = ''
                for _ in range(repr2):
                    processed_data += data
#                print('Getting ld for',processed_data)
                ld = get_decompress_len_v2(processed_data)
#                print('ld', ld)
                l += ld
            else:
                l += repr1 * repr2
            continue
#        print(c)
        l += 1
#    print(f'>L = {l}')
#    print()
    return l


# (3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no markers.
assert get_decompress_len_v2('(3x3)XYZ') == 9
# X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker is then further decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
assert get_decompress_len_v2('X(8x2)(3x3)ABCY') == 20
# (27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 241920 times.
assert get_decompress_len_v2('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
# (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long.
assert get_decompress_len_v2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445

answer = get_decompress_len_v2(line.strip())
print(answer)

