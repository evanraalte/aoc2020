import os
import re
from math import ceil,gcd
from functools import reduce # Python version 3.x
from itertools import product  

# aba
# aab
vec = {}
def set_vec(pos,val):
    if not pos in vec:
        vec[pos] = False
    if vec[pos] == False:
        vec[pos] = val

def reset_vec():
    vec = {}
def check(message,deps, dep_num = 0, pos = 0,first=False):
    try:
        dep = deps[dep_num]
    except KeyError:
        dep = dep_num
        
    if isinstance(dep,tuple):
        for d in dep:
            (valid,pos) = check(message,deps,d,pos)
            if not valid:
                if first and len(message) == len(vec) and all(vec.values()):
                    pass
                    # print(vec)
                    # reset_vec()
                    # return (True,pos)
                return (False,None)
        if first:
            if len(message) == pos:
                print(message)
                reset_vec()
                return (True,pos)
            else: 
                return (False,None)    
        return (True,pos)  
    elif isinstance(dep,list): 
        left  = check(message,deps,dep[0],pos)
        right = check(message,deps,dep[1],pos)
        # print(left,right)
        if left[0]:
            return left
        elif right[0]:
            return right
        else:
            return (False,None)
    elif isinstance(dep,str):
        try:
            ret = message[pos] == dep
            set_vec(pos,ret)
            # if ret:
                # print(f"matching {message[pos]} == {dep} at pos {pos}: {message[pos] == dep}")
            return (ret,pos+1)
        except IndexError:
            return (False,None)

def part1(messages,deps):
    # checks = generate_from_rules(deps)
    s = sum(check(message,deps,0,first=True)[0] for message in messages)
    # print(f"msg: {vec}")
    return s
def part2(messages,deps):
    return part1(messages,deps)


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day19-test.txt")) as f:
    rules,messages = tuple(x.split('\n') for x in f.read().split('\n\n'))
    rules =  {int(x[0]) : x[1] for x in [ re.match(r'^(\d+): (.*)$',rule).groups() for rule in rules]}

    deps = {}
    for k,rule in rules.items():
        m = re.match(r'"(\w)"',rule)
        if m:
            deps[k] = m.group(1)
        elif "|" in rule:
            sub_rules = rule.split("|")
            sub_rule_list = []
            for sub_rule in sub_rules:
                sub_rule_list.append(tuple(map(int,filter(lambda x: x!= '', sub_rule.split(" "))))   )
            deps[k] = sub_rule_list
        else:
            deps[k] = tuple(map(lambda x: int(x),rule.split(" ")))



    p1 = part1(messages,deps)
    print(f"Part 1: {p1}")

    deps[8] =  [(42,) , (42,8)]   
    deps[11] =  [(42,31), (42,11,31)]

    p2 = part2(messages,deps)
    print(f"Part 2: {p2}")
