import os
import re
from math import ceil,gcd
from functools import reduce # Python version 3.x
from itertools import product

def part1(d):
    mem = {}
    for l in d:
        m = re.match(r'^mask = ([10X]{36})$',l)
        if m:
            mask = int(m.group(1).replace('1','0').replace('X','1'),2) # actually a mask
            opr  = int(m.group(1).replace('X','0'),2)

        else:
            m = re.match(r'^mem\[(\d+)\] = (\d+)$',l).groups()
            mem[m[0]] = (int(m[1]) & mask) + opr 
        pass
    return sum(mem.values())

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def str_mask(num,mask):
    num = "{:036b}".format(int(num))
    res = [None]*36

    for i in range(0,36):
        res[i] = mask[i] if mask[i] > num[i] else num[i]
    return "".join(res)

def permute(s):
    idxs = find(s,'X')
    cp   = list(product("01",repeat=len(idxs)))   
    addresses = []
    for p in cp:
        address = [c for c in s]
        for i,e in enumerate(p): # for every entry in the tuple
            address[idxs[i]] = e
        addresses.append(int("".join(address),2))
    return addresses

def part2(d): 
    mem = {}
    for l in d:
        m = re.match(r'^mask = ([10X]{36})$',l)
        if m:
            mask = m.group(1)
        else:
            m = re.match(r'^mem\[(\d+)\] = (\d+)$',l).groups()
            addresses = permute(str_mask(m[0],mask))
            for a in addresses:
                mem[a] = int(m[1])

    return sum(mem.values())



ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day14.txt")) as f:
    d = f.readlines()
    p1 = part1(d)
    print(f"Part 1: {p1}")

    p2 = part2(d)
    print(f"Part 2: {p2}")