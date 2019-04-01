# python3
from collections import defaultdict


def solve(line):
    return parse(line, 0)

def parse(s, level):
    points = 0
    idx = 0
    while s[idx] != '{':
        idx += 1
    parse(s[idx:], level + 1)
    return points

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readlines()
    solution = solve(inp)
    print(solution)
