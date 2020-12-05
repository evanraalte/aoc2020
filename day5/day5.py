import os
import re

def part1(d):
    return max(d)

def part2(d):
    rows = [(e & 0x3FC) >> 3 for e in d]
    tickets = d
    seats   = range((min(rows)+1)*8,(max(rows)-1)*8)

    return  (set(seats) & set(tickets)) ^ set(seats)

ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day5.txt")) as f:
    d = [int("".join([str(ord(z)%7%2) for z in y]),2) for y in f.read().split("\n")]
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")