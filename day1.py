def part1(data):
    for i in range(0,len(data)):
        for j in range(i,len(data)):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]

def part2(data):
    for i in range(0,len(data)):
        for j in range(i,len(data)):
            for k in range(j,len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]

with open("day1.txt") as f:
    data = [int(i) for i in f.read().splitlines()]   
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

