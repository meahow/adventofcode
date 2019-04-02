# python3


def solve(line):
    parsed = parse(line)
    return parsed[1]

def parse(s, idx=0, level=0):
    print(f"level={level}, idx='{idx}'")
    points = level
    while idx < len(s):
        if s[idx] == '!':
            idx += 2
        elif s[idx] == '{':
            idx, new_points = parse(s, idx + 1, level + 1)
            points += new_points
        elif s[idx] == '}':
            return idx + 1, points
        elif s[idx] == '<':
            idx = skip_garbage(s, idx + 1)
        else:
            idx += 1
    return idx, points

def skip_garbage(s, idx):
    while idx < len(s):
        if s[idx] == '!':
            idx += 2
        elif s[idx] == '>':
            break
        else:
            idx += 1
    return idx

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readline()
    solution = solve(inp)
    print(solution)
