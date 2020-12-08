from itertools import count
import os
import re

def check_shiny_gold(bag_name, bags):
    if bags[bag_name] == {}: # End condition
        return 0
    if "shiny gold" in bags[bag_name]:
        return 1
    # If not found directly, check it through the other bags
    return any(map(lambda x: check_shiny_gold(x,bags),bags[bag_name].keys()))    


def count_bags_in(bag_name, bags):
    if bags[bag_name] == {}: # End condition, contains no bags
        return 0
    return sum(int(num) * (count_bags_in(child_bag_name,bags) + 1) for child_bag_name,num in bags[bag_name].items())

def part1(bags):
    return sum(check_shiny_gold(bag_name, bags) for bag_name in bags.keys())


def part2(bags):
    return count_bags_in("shiny gold",bags)


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day7.txt")) as f:
    d = [re.search(r'^(\w+ \w+) bags contain (.+)$',x).groups() for x in f.read().split('\n')]
    bags = {bag: {b: a  for (a,b) in re.findall(r'(\d+) (\w+ \w+) bags?',contents)} for (bag,contents) in d}

    print(f"Part 1: {part1(bags)}")
    print(f"Part 1: {part2(bags)}")