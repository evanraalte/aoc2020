import os
import re


def run_program(d):
    pc = 0
    coverage = set()
    acc = 0
    error = 0
    done = 0

    while not (error or done):
        instr, arg = d[pc]
        coverage.add(pc)
        if instr == "nop":
            pc = pc + 1
        elif instr == "acc":
            acc += int(arg)
            pc  += 1
        elif instr == "jmp":
            pc += int(arg)
        error = pc in coverage
        done  = pc == len(d)
    print((acc,error))
    return (acc,error)

def part1(d):
    return run_program(d)[0]


lut = {
    "nop": "jmp",
    "jmp": "nop"
}

def part2(d):
    for i in range(0,len(d)):
        if d[i][0] == "nop":
            modified_program = d[:] # hardcopy!
            modified_program[i] = ("jmp",d[i][1])
        elif d[i][0] == "jmp":
            modified_program = d[:] # hardcopy!
            modified_program[i] = ("nop",d[i][1])
        else: 
            continue
        acc,err = run_program(modified_program)
        if err == 0:
            return acc

    return 0


ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day8.txt")) as f:
    d = [re.search(r'^(\w+) ([-+]\d+)$',l).groups() for l in f.read().split('\n')]
    

    # print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")