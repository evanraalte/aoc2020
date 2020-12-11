import os
import re
import itertools
# from functools import lru_cache
# from igraph import *

def check_free(p,d,part2=False):
    px,py = p
    adj = [(0, -1), (0, 1), (-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1)]
    
    seats = {'L' : 0, '.': 0, '#': 0}
    if part2:
        seats_to_check = []
        for a in adj:
            seats[extrapolate(a,p,d)] += 1
    else:
        for a in adj:
            ax,ay = a
            x = ax + px
            y = ay + py
            if (x,y) in d:
                seats[d[(x,y)]] += 1 
            else: # outside of defined area, free area I guess
                seats['.'] += 1
    return seats['L'] + seats['.']



def assign(num_free, cur_state, tolerance):
    if cur_state == 'L' and num_free == 8:
        return '#'
    if cur_state == '#' and num_free <= tolerance:
        return 'L'
    return cur_state

def print_grid(d):
    xs = [x for (x,y) in d.keys()]
    ys = [y for (x,y) in d.keys()]

    for y in range(0,max(xs)+1):
        lbuf = ""
        for x in range(0,max(xs)+1):
            lbuf+=d[(x,y)]
        print(lbuf)
    print('\n')

def converge(d, part2 = False):
    stable = False
    old    = -1
    new    = -1

    if part2:
        tolerance = 8-5 # leave at >=5 occupied seats
    else:
        tolerance = 8-4 # leave at >=4 occupied seats

    while not stable:
        old = new
        num_map = {k : check_free(k,d,part2) for k,v in d.items()}
        d   =  {k : assign(v,d[k],tolerance) for k,v in num_map.items()}
        new = sum(1 for v in d.values() if v == '#') 
        # print_grid(d)
        stable = (old == new)
    return new

def part1(d):
    return converge(d)


def extrapolate(direction,pos,d):
    res = '.'
    dx,dy = direction
    px,py = pos
    x,y   = (px+dx,py+dy)
    while (x,y) in d:
        res = d[(x,y)]
        if res in ['#','L']:
            return res
        x += dx
        y += dy
    return res

def part2(d):
    return converge(d,part2=True)


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"/Users/Erik van Raalte/Documents/aoc2020/day11/day11.txt")) as f:
    d = { (x,y) : v for y,l in enumerate(f.read().split('\n')) for x,v in enumerate(l)} 
    p1 = part1(d.copy())
    print(f"Part 1: {p1}")
    p2 = part2(d)
    print(f"Part 2: {p2}")