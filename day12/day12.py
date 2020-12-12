import os
import re
import itertools
from math import sin,cos,radians
# from functools import lru_cache
# from igraph import *


def part1(d):
    dirs = {'E' : (1,0),'S' : (0,-1),'W': (-1,0),'N' : (0,1)}
    dir  = 'E'
    px,py = 0,0
    for instr,arg in d:
        if instr in (list(dirs.keys()) + ['F']):
            dx,dy = dirs[dir] if instr == 'F' else dirs[instr]
            px += dx*arg
            py += dy*arg
        else:
            bdk = list(dirs.keys())
            dir_idx = bdk.index(dir)
            n = int(arg/90)
            if instr == 'R':
                dir = bdk[(dir_idx + n)%len(bdk)]
            else:
                dir = bdk[(dir_idx + len(bdk) - n)%len(bdk)]
        print(f"pos: ({px},{py})")

    return abs(px) + abs(py)

def part2(d):
    dirs = {'E' : (1,0),'S' : (0,-1),'W': (-1,0),'N' : (0,1)}
    px,py = 0,0
    wx,wy = 10,1
    for instr,arg in d:
        if instr in dirs.keys():
            dx,dy = dirs[instr]
            wx,wy = (wx + dx*arg,wy + dy*arg)
        elif instr == 'F':
            px,py = (px + wx*arg,py + wy*arg)
        else:
            n = int(arg/90)
            r = (1,-1) if instr =='R' else (-1,1)
            while n>0: # rotate 90 degrees n times
                wx,wy =  (r[0]*wy,r[1]*wx)  
                n -= 1
            
        print(f"pos: ({px},{py}), waypoint: ({wx},{wy}), instr: {instr}, arg: {arg}")

    return abs(px) + abs(py)


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day12.txt")) as f:
    d = [ (l[0],int(l[1:])) for l in f.read().split('\n') ]
    p1 = part1(d)
    print(f"Part 1: {p1}")
    p2 = part2(d)
    print(f"Part 2: {p2}")