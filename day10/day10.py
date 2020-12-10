import os
import re
from functools import lru_cache

def part1(d):
    jolts = 0
    diffs = {1 : 0, 2 : 0, 3 : 0}
    while (len(d)): # while our input set still contains values
        for i in range(1,3+1):
            if (jolts + i) in d:
                diffs[i] += 1
                d.remove(jolts + i)
                jolts += i
                # print(f"difference: {i}, {jolts - i} -> {jolts} ")
                break  
    return diffs[1] * (diffs[3] + 1)


lut = {}
def m(k,stop,deps):
    if k == stop: # this is the only ending path that is valid
        return 1
    elif k in lut:
        return lut[k]
    else:
        val = sum(m(n,stop,deps) for n in deps[k])
        lut[k] = val
        # print(f"k={k}, deps={deps[k]}, m({k}) = {val}")
        return val

def part2(d):
    d.add(0) # start position
    deps = dict.fromkeys(d, {})
    for node in deps.keys():
        deps[node] = {a for a in deps.keys() if node + 1 <= a <= node + 3 }
    
    stop = list(deps.keys())[-1]
    return m(0,stop,deps)


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"/Users/Erik van Raalte/Documents/aoc2020/day10/day10.txt")) as f:
    d = set([int(l) for l in f.read().split('\n')])
    p1 = part1(d.copy())
    print(f"Part 1: {p1}")
    p2 = part2(d)

    print(f"Part 2: {p2}")