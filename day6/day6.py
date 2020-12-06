import os
import re

def part1(d):
    s = 0
    for e in d:
        e = e.replace('\n','')
        letters = {}
        for l in e:
            if l not in letters:
                letters[l] = True
        s += len(letters.keys())
    return s

def part2(d):
    s = 0
    for e in d:
        req_len = e.count("\n") + 1
        e = e.replace('\n','')
        letters = {}
        for l in e:
            if l not in letters:
                letters[l] = 1
            else:
                letters[l] += 1
        s+= sum(1 for x in letters.values() if x == req_len)
    return s 


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day6.txt")) as f:
    d = f.read().split("\n\n")
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")