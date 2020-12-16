import os
import re
from math import ceil,gcd
from functools import reduce # Python version 3.x
from itertools import product

def part1(c,nts):
    s = 0
    for nt in nts: # for every ticket
        for n in nt: # for every value in a ticket
            if not any(map(lambda x: x(n),c.values())):
                s += n
    return s

def part2(c,nts,mt):
    to_delete = []
    for nt in nts: # for every ticket
        for n in nt: # for every value in a ticket
            if not any(map(lambda x: x(n),c.values())):
                to_delete.append(nts.index(nt))
                break

    to_delete.reverse()
    for td in to_delete:
        nts.pop(td)
    # Now all in NTS is valid

    # Transpose for easier looping
    nts_t = list(map(list, zip(*nts)))

    ticket_fields = {}
    field_names = list(c.keys())
    while c != {}: # while we still have to allocate
        for idx,d in enumerate(nts_t):
            possibilities = []
            for name,f in c.items():
                if all(map(lambda x: f(x),d)):
                    possibilities.append(name)
            if len(possibilities) == 1: # only assign when it is the only possiblity
                ticket_fields[possibilities[0]] = idx
                del c[possibilities[0]] # no need to check anymore

    res = 1
    for fn in field_names:
        if "departure" in fn:
            idx = ticket_fields[fn] # index of field that start with departure
            res *= mt[idx]
            pass

    return res

def return_lambda(n0,n1,n2,n3):
    return lambda x: (int(n0) <= x <= int(n1)) or (int(n2) <= x <= int(n3))

ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day16.txt")) as f:
    criteria = {}
    lines = f.read().split('\n')
    si = [0] + [idx for idx,v in enumerate(lines) if v == ''] + [len(lines)]

    # reading criteria
    for l in lines[si[0]:si[1]]:
        (name,n0,n1,n2,n3) = re.match(r'^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)$',l).groups()
        criteria[name] = return_lambda(n0,n1,n2,n3) #needed: https://stackoverflow.com/questions/50298582/why-does-python-asyncio-loop-call-soon-overwrite-data
        pass

    # reading my ticket
    my_ticket = [int(i) for i in lines[si[1]+2].split(',')]

    # reading nearby tickets
    nearby_tickets = []
    for l in lines[si[2]+2:si[3]]:
        nearby_tickets.append([int(i) for i in l.split(',')])
    p1 = part1(criteria,nearby_tickets)
    print(f"Part 1: {p1}")

    p2 = part2(criteria,nearby_tickets,my_ticket)
    print(f"Part 2: {p2}")
