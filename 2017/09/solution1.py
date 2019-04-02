# python3
from collections import defaultdict


def solve(line):
    return parse(line, 0)

def parse(s, level):
    points = level
    idx = 0
    while idx <= len(s) < 1:
        if s[idx] == '{':
            new_idx, new_points = parse(s[idx + 1:], level + 1)
            points += new_points
            idx += new_idx
        else:
            idx += 1
    return idx, points

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readlines()
    solution = solve(inp)
    print(solution)
