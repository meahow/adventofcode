# python3


def solve(line):
    parsed = parse(line)
    return parsed[2]

def parse(s, idx=0, level=0, skipped=0):
    print(f"level={level}, idx='{idx}'")
    points = level
    while idx < len(s):
        if s[idx] == '!':
            idx += 2
        elif s[idx] == '{':
            idx, new_points, new_skipped = parse(s, idx + 1, level + 1)
            points += new_points
            skipped += new_skipped
        elif s[idx] == '}':
            return idx + 1, points, skipped
        elif s[idx] == '<':
            idx, new_skipped = skip_garbage(s, idx + 1)
            skipped += new_skipped
        else:
            idx += 1
    return idx, points, skipped

def skip_garbage(s, idx):
    skipped = 0
    while idx < len(s):
        if s[idx] == '!':
            idx += 2
        elif s[idx] == '>':
            break
        else:
            skipped += 1
            idx += 1
    print("skipping %s chars at %s" % (skipped, idx))
    return idx, skipped

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readline()
    solution = solve(inp)
    print(solution)
