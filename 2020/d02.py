import re
from collections import Counter

total = 0
with open('d02.input') as f:
    for line in f.readlines():
        line = line.strip()
#        print(line)
        m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
        f, t, l, hay = m.groups()
        print(f, t, l, hay)
        c = Counter(hay)
        print(c)
        if int(f) <= c[l] <= int(t):
            total += 1
print(total)

