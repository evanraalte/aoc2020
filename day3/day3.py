import os
import re
import functools
import operator

def traverse(d, v):
    return len([x for x in[ (d[v[1]*i][v[0]*i % len(d[0])]) for i in range(0,round(len(d)/v[1]))] if x == '#'])

# def traverse(d, v, p = (0,0)):
#     vx,vy = v
#     px,py = p

#     len_line = len(d[0])
#     is_tree = lambda c : d[ c[0] ][ (c[1] % len_line) ] == '#'

#     num_trees = 0
#     while py < len(d): # while not all the way down:
#         if is_tree((py,px)):
#             num_trees += 1
#         px += vx
#         py += vy
#     return num_trees

def part1(d):
    return traverse(d,(3,1))
def part2(d):
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    return functools.reduce(operator.mul,map(lambda v: traverse(d,v),slopes))

ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day3.txt")) as f:
    d = f.read().splitlines()
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")
