import os
import re
from math import ceil,gcd
from functools import reduce # Python version 3.x
from itertools import product

def get_next_state(xyz,state,d,neighbours):
    x,y,z = xyz
    active = sum(1 for (dx,dy,dz) in neighbours if (x+dx,y+dy,z+dz) in d and d[(x+dx,y+dy,z+dz)] == '#')

    if state =='#':
        if (active == 2 or active == 3):
            state_next = state
        else:
            state_next = '.'

    elif state =='.':
        if active == 3:
            state_next = '#'
        else:
            state_next = state

    return state_next

def get_next_state_2(xyzw,state,d,neighbours):
    x,y,z,w = xyzw
    active = sum(1 for (dx,dy,dz,dw) in neighbours if (x+dx,y+dy,z+dz,w+dw) in d and d[(x+dx,y+dy,z+dz,w+dw)] == '#')

    if state =='#':
        if (active == 2 or active == 3):
            state_next = state
        else:
            state_next = '.'

    elif state =='.':
        if active == 3:
            state_next = '#'
        else:
            state_next = state

    return state_next

def iterate(d,neighbours):
    coords = []
    for (x,y,z) in d.keys():
        for (dx,dy,dz) in neighbours:
            xyz = (x+dx,y+dy,z+dz) 
            if not xyz in d:
                coords.append(xyz)

    for c in coords:
        d[c] = '.'

    d_next = {}
    for xyz,state in d.items():
        d_next[xyz] = get_next_state(xyz,state,d,neighbours)

    return d_next

def iterate_2(d,neighbours):
    coords = []
    for (x,y,z,w) in d.keys():
        for (dx,dy,dz,dw) in neighbours:
            xyzw = (x+dx,y+dy,z+dz,w+dw) 
            if not xyzw in d:
                coords.append(xyzw)

    for c in coords:
        d[c] = '.'

    d_next = {}
    for xyzw,state in d.items():
        d_next[xyzw] = get_next_state_2(xyzw,state,d,neighbours)

    return d_next

def part1(d):
    d_n = d

    neighbours = list(product([-1,0,1],repeat=3))
    neighbours.pop(neighbours.index((0,0,0)))

    for i in range(0,6):
        bound_x = min(d_n.keys(),key=lambda x : x[0]), max(d_n.keys(),key=lambda x : x[0])
        bound_y = min(d_n.keys(),key=lambda x : x[1]), max(d_n.keys(),key=lambda x : x[1])
        bound_z = min(d_n.keys(),key=lambda x : x[2]), max(d_n.keys(),key=lambda x : x[2])

        # print(f"len: {len(d_n.keys())}, x: {bound_x}, y: {bound_y}, z: {bound_z}")
        d_n = iterate(d_n,neighbours)
        print(f"count # after {i+1} cycle: {list(d_n.values()).count('#')}")
    return list(d_n.values()).count('#')

def part2(d):
    d_n = d

    neighbours = list(product([-1,0,1],repeat=4))
    neighbours.pop(neighbours.index((0,0,0,0)))

    for i in range(0,6):
        bound_x = min(d_n.keys(),key=lambda x : x[0]), max(d_n.keys(),key=lambda x : x[0])
        bound_y = min(d_n.keys(),key=lambda x : x[1]), max(d_n.keys(),key=lambda x : x[1])
        bound_z = min(d_n.keys(),key=lambda x : x[2]), max(d_n.keys(),key=lambda x : x[2])
        bound_w = min(d_n.keys(),key=lambda x : x[3]), max(d_n.keys(),key=lambda x : x[3])

        # print(f"len: {len(d_n.keys())}, x: {bound_x}, y: {bound_y}, z: {bound_z}")
        d_n = iterate_2(d_n,neighbours)
        print(f"count # after {i+1} cycle: {list(d_n.values()).count('#')}")
    return list(d_n.values()).count('#')

ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day17.txt")) as f:
    raw = f.read().split('\n')
    d1 = { (x,y,0) : v for y,l in enumerate(raw) for x,v in enumerate(l)}
    p1 = part1(d1)
    print(f"Part 1: {p1}")


    d2 = { (x,y,0,0) : v for y,l in enumerate(raw) for x,v in enumerate(l)}
    p2 = part2(d2)
    print(f"Part 2: {p2}")
