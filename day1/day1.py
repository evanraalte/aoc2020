import os
import functools
import itertools
import operator


def find2020(data,num_elements):
    return functools.reduce(operator.mul, next(filter(lambda x: sum(x) == 2020, itertools.combinations(data,num_elements))),1)

def part1(data):
    return find2020(data,2)

def part2(data):
    return find2020(data,3)

ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day1.txt")) as f:
    data = [int(i) for i in f.read().splitlines()]   
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

