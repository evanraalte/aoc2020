import os
import re

def chk_height(data):
    try:
        (h,e) = tuple(re.search(r'^(\d{2,3})(cm|in)$',data).groups())
        return (150 <= int(h) <= 193 ) if e == "cm" else (59 <= int(h) <= 76 )
    except Exception:
        return False
checkers = {
    "byr" : lambda x: 1920 <= int(x) <= 2002,
    "iyr" : lambda x: 2010 <= int(x) <= 2020,
    "eyr" : lambda x: 2020 <= int(x) <= 2030,
    "hgt" : lambda x: chk_height(x),
    "hcl" : lambda x: re.search(r'^#[\da-f]{6}$',x) != None,
    "ecl" : lambda x: x in ["amb","blu","brn","gry","grn","hzl","oth"],
    "pid" : lambda x: re.search(r'^[\d]{9}$',x) != None,
    "cid" : lambda x: True
}

required = list(checkers.keys())[:-1]

def part1(d):
    return  len([x for x in map(lambda x: re.findall(r'([a-z]{3}):(#?\w+)',x),d) if all([ (t in map(lambda a: a[0],x)) for t in required ])])


def part2(d):
    return  len([x for x in map(lambda x: re.findall(r'([a-z]{3}):(#?\w+)',x),d) if all([ (t in map(lambda a: a[0],x)) for t in required ])  and all(map(lambda a: checkers[a[0]](a[1]),x))  ])

ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day4.txt")) as f:
    d = f.read().split("\n\n")
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")
