import os
import re
from math import ceil,gcd
from functools import reduce # Python version 3.x
from itertools import product

def spoken_at_n(n,d):
    t = 0
    mem = {}
    time_since_spoken = 0
    for _d in d:
        time_since_spoken = t - mem[_d] if _d in mem else 0
        mem[_d] = t
        t += 1
    
    s = 0
    while t < n:
        s = time_since_spoken
        time_since_spoken = t - mem[s] if s in mem else 0
        mem[s] = t
        t += 1
    return s

def part1(d):
    return spoken_at_n(2020,d)

def part2(d): 
    return spoken_at_n(30000000,d)



ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day15-test.txt")) as f:
    d = [int(n) for n in f.readline().split(',')]
    p1 = part1(d)
    print(f"Part 1: {p1}")

    p2 = part2(d)
    print(f"Part 2: {p2}")