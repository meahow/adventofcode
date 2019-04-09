# python3


def solve(layers):
    severities = []
    for layer in layers:
        parts = map(lambda s: int(s.strip(':')), layer.split())
        depth, range_ = parts
        caught = depth % (range_ * 2 - 2) == 0
        if caught:
            severities.append(depth * range_)
    return sum(severities)


if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readlines()
    solution = solve(inp)
    print(solution)
