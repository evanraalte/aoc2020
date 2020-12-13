import os
import re
from math import ceil,gcd
from functools import reduce # Python version 3.x


def part1(ts,d):
    a = min([(ceil(ts/b)*b,b) for b in d if ceil(ts/b)*b >= ts],key= lambda x: x[0])
    return (a[0]-ts)*a[1]

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)


def part2(d): 
    nums = []
    p = d[0][1] # second period of first bus
    nums.append(p)
    for i in range(1,len(d)):
        n = 0
        pf = []
        while d[i][1] not in pf:
            n+=1
            pf = prime_factors(p+lcm(nums)*n+d[i][0])
        lcm_nums = lcm(nums)
        nums.append(d[i][1])
        p = p + lcm_nums*n
    return p

# better solution (from someone else):
# def Part2():
#     t = 0
#     m = 1
#     for (i, p) in schedule:
#         while (t + i) % p:
#             t += m
#         m *= p
#     return t


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day13.txt")) as f:
    ts = int(f.readline())
    d = f.readline().split(',')
    d1 = [ int(l) for l in d if l != 'x']
    p1 = part1(ts,d1)
    print(f"Part 1: {p1}")


    d2 = list(enumerate([ int(l) if l!='x' else 'x' for l in d]))
    d2 = [x for x in d2 if x[1]!= 'x']
    p2 = part2(d2)
    print(f"Part 2: {p2}")