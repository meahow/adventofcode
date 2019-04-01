# python3
from collections import defaultdict


def solve(lines):
    registers = defaultdict(int)
    total_max = 0
    for line in lines:
        # line format: "b inc 5 if a > 1"
        parts = line.split()
        current_reg, command, value, _, cond_reg, cond_operator, cond_value = parts
        # condition
        cond_str = "%s %s %s" % (registers[cond_reg], cond_operator, cond_value)
        print(cond_str)
        if eval(cond_str):
            print("passed")
            if command == 'inc':
                registers[current_reg] += int(value)
            elif command == 'dec':
                registers[current_reg] -= int(value)
            else:
                raise ValueError("invalid command %s" % command)
            total_max = max(total_max, registers[current_reg])
    print(registers.items())
    return total_max

if __name__ == '__main__':
    with open("input.txt") as infile:
        graph = infile.readlines()
    solution = solve(graph)
    print(solution)
