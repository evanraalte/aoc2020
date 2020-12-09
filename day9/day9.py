import os
import re

def part1(d):
    plen = 25
    for i,v in enumerate(d[plen:]):
        nums = d[i :i + plen]
        sums = set([x+y for x in nums for y in nums])
        if v not in sums:
            return v

def part2(d,p1):
    d = [a for a in d if a < p1 ] # no need to look at larger numbers
    n = 3
    val = False
    while not val: #
        val = next((min(d[i:i+n]) + max(d[i:i+n]) for i in range(0,len(d)-n) if sum(d[i:i+n]) == p1),False)
        n += 1
    return val


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day9.txt")) as f:
    d = [int(l) for l in f.read().split('\n')]
    p1 = part1(d)
    print(f"Part 1: {p1}")
    print(f"Part 2: {part2(d,p1)}")