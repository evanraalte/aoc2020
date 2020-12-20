import os
import re
from math import ceil,gcd
from functools import reduce # Python version 3.x
from itertools import product  

# aba
# aab

def check(message,deps, dep_num = 0, pos = 0,first=False):
    try:
        dep = deps[dep_num]
    except KeyError:
        dep = dep_num
    # print(f"dep: {dep} (dep {dep_num}, pos: {pos}, msg: {message}")
    if isinstance(dep,tuple):
        for d in dep:
            (valid,pos) = check(message,deps,d,pos)
            # print(f"d: {d}, valid: {valid}, pos: {pos}")
            if not valid:
                return (False,None)
        pass
        if first:
            if len(message) == pos:
                print(f"pos: {pos}, matches length!")
                return (True,pos)
            else: 
                return (False,None)
        
        return (True,pos)
        
        # if first and len(message) == pos:
        # else:
        #     return (False,None)
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

        # return all(map(lambda x: check(message,deps,x[0],x[1]),zip(dep[0],pos))) or all(map(lambda x: check(message,deps,x[0],x[1]),zip(dep[1],pos)))
    elif isinstance(dep,int):
        return check(message,deps,dep,pos)
    elif isinstance(dep,str):
        try:
            ret = message[pos] == dep
            # print(f"matching {message[pos]} == {dep} at pos {pos}: {message[pos] == dep}")
            return (ret,pos+1)
        except IndexError:
            return (False,None)

# def generate_from_rules(deps, rule_num = "0"):
#     ret = []
#         print(deps[rule_num])
#         ret.append("".join([generate_from_rules(deps,x) for x in deps[rule_num]]))
#     if isinstance(deps[rule_num],list):
        
#         for d in deps[rule_num]:
            
#     if isinstance(deps[rule_num],str) and  deps[rule_num] in "ab":
#         return deps[rule_num]

#     return ret

def part1(messages,deps):
    # checks = generate_from_rules(deps)
    return sum(check(message,deps,0,first=True)[0] for message in messages)
    # return 0
def part2(d):
    
    return 0


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

    # p2 = part2(d)
    # print(f"Part 2: {p2}")
