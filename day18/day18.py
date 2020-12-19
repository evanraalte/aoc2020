import os
import re
from math import ceil,gcd
from functools import reduce # Python version 3.x
from itertools import product

class Token:
    def __str__(self):
        return f"kind: {self.kind}, value: {self.value}"
    def __init__(self,kind,value = None):
        self.kind  = kind
        self.value = value

class Token_stream:
    def __init__(self,stream):
        self.buf  = None
        self.full = False
        self.stream = [c for c in stream]

    def pop_from_stream(self):
        try:
            return self.stream.pop(0)
        except Exception:
            return None
    def get(self):
        if self.full:
            self.full = False
            return self.buf

        if len(self.stream) == 0:
            return Token(None,None)

        buf = []
        v = self.pop_from_stream()
        if v in "+*()":
            # print(f'return {Token(v)}')
            return Token(v)
        elif v in "01234567890":
            self.stream.insert(0,v) # push back into stream
            while True:
                v = self.pop_from_stream()
                if v and v in "1234567890":
                    buf.append(v)
                else:
                    if v: # insert last one back if it was not None
                        self.stream.insert(0,v) 
                    # print(f'return {Token("int",int("".join(buf)))}')
                    return Token("int",int("".join(buf)))
        else:
            raise Exception("Bad token")
    def push_back(self,t):
        assert self.full == False
        self.buf = t
        self.full = True

def expression(ts):
    left = primary(ts) 
    t    = ts.get()
    while True:
        if t.kind == '+':
            exp = primary(ts)
            left += exp
            t = ts.get()
        elif t.kind == '*':
            exp = primary(ts)
            left *= exp
            t = ts.get()
        else:     
            ts.push_back(t)
            return left   

    
def primary(ts):
    t = ts.get()
    if t.kind == "(":
        d = expression(ts)
        t = ts.get()
        assert t.kind == ")"
        return d
    elif t.kind == "int":
        return t.value
    else:
        raise Exception("Bad token")



def term_adv(ts):
    left = primary_adv(ts)
    t = ts.get()
    while True:
        if t.kind == '+':
            left +=primary_adv(ts)
            t = ts.get()
        else:
            ts.push_back(t)
            return left

def expression_adv(ts):
    left = term_adv(ts) 
    t    = ts.get()
    while True:
        if t.kind == '*':
            exp = term_adv(ts)
            left *= exp
            t = ts.get()
        else:     
            ts.push_back(t)
            return left   

    
def primary_adv(ts):
    t = ts.get()
    if t.kind == "(":
        d = expression_adv(ts)
        t = ts.get()
        assert t.kind == ")"
        return d
    elif t.kind == "int":
        return t.value
    else:
        raise Exception("Bad token")



def part1(d):
    s = 0
    for e in d:
        ts = Token_stream(e)
        s += expression(ts)
    return s
def part2(d):
    s = 0
    for e in d:
        ts = Token_stream(e)
        s += expression_adv(ts)
    return s  


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day18.txt")) as f:
    d = [x.replace(' ','') for x in f.read().split('\n')]
    
    p1 = part1(d)
    print(f"Part 1: {p1}")

    p2 = part2(d)
    print(f"Part 2: {p2}")
