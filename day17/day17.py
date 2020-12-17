import os
import re
from math import ceil,gcd
from functools import reduce # Python version 3.x
from itertools import product

add_t = lambda x,y : tuple(map(sum,zip(x,y)))

def get_next_state(c,state,d,neighbours):
    active = sum(1 for d_c in neighbours if d.get(add_t(c,d_c)) == '#')
    state_next = state
    if state =='#' and not (active == 2 or active == 3):
            state_next = '.'
    elif state =='.' and active == 3:
        state_next = '#'
    return state_next


def iterate(d,neighbours):
    coords = []
    for c in d.keys(): # should only check when >0 dimensions are maxed
        for d_c in neighbours:
            c_n = add_t(c,d_c) 
            if not c_n in d:
                coords.append(c_n)

    for c in coords:
        d[c] = '.'

    d_next = {}
    for c,state in d.items():
        d_next[c] = get_next_state(c,state,d,neighbours)

    return d_next

def iterate_six(d,dims):
    d_n = { tuple([x,y] +[0]*(dims-2)) : v for y,l in enumerate(d) for x,v in enumerate(l)}
    neighbours = list(product([-1,0,1],repeat=dims))
    neighbours.pop(neighbours.index( tuple([0]*dims)  ))

    for _ in range(0,6):
        d_n = iterate(d_n,neighbours)
    return list(d_n.values()).count('#')

def part1(d):
    return iterate_six(d,3)
def part2(d):
    return iterate_six(d,4)


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day17.txt")) as f:
    d = f.read().split('\n')
    
    p1 = part1(d)
    print(f"Part 1: {p1}")

    p2 = part2(d)
    print(f"Part 2: {p2}")
