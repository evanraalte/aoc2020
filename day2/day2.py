import os
import re

def part1(d):
    return len(list(filter(lambda x : int(x[0]) <= x[3].count(x[2]) <= int(x[1]),d)))

def part2(d):
    return len(list(filter(lambda x : (x[3][int(x[0])-1] == x[2]) ^ (x[3][int(x[1])-1] == x[2]),d)))

ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day2.txt")) as f:
    d = re.findall(r'(\d+)-(\d+) ([a-z]): ([a-z]+)',f.read())
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")
