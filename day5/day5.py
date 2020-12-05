import os
import re

def part1(d):
    return max([mul(e) for e in d])
    pass
def part2(d):
    rows = [e[0] for e in d]
    tickets = [mul(e) for e in d]
    seats   = range((min(rows)+1)*8,(max(rows)-1)*8)

    return  (set(seats) & set(tickets)) ^ set(seats)
    


def to_row(s):
    return int(s.replace('F','0').replace('B','1'),2)

def to_col(s):
    return int(s.replace('L','0').replace('R','1'),2)

def mul(t):
    return t[0]*8+t[1]

ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day5.txt")) as f:
    d = [(to_row(a),to_col(b)) for x in f.read().split("\n") for (a,b) in re.findall(r'([FB]{7})([LR]{3})', x) ]
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")