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
    return 0


def count_bags_in(bag_name, bags):
    if bags[bag_name] == {}: # End condition, contains no bags
        return 0
    num_bags = 0
    for child_bag_name,num in bags[bag_name].items():
        num_bags += int(num)
        num_bags += int(num)*count_bags_in(child_bag_name,bags)   
    return num_bags


def part1(bags):
    count = 0
    for bag_name in bags.keys():
        count += check_shiny_gold(bag_name, bags)
    return count


def part2(bags):
    return count_bags_in("shiny gold",bags)


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day7.txt")) as f:
    d = [re.search(r'^(\w+ \w+) bags contain (.+)$',x).groups() for x in f.read().split('\n')]

    bags = {}
    for bag,contents in d:
        bags[bag] = {b: a  for (a,b) in re.findall(r'(\d+) (\w+ \w+) bags?',contents)}
    print(f"Part 1: {part1(bags)}")
    print(f"Part 1: {part2(bags)}")