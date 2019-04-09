# python3


def solve(layers):
    delay = 0
    layerlist = []
    for layer in layers:
        parts = map(lambda s: int(s.strip(':')), layer.split())
        depth, range_ = parts
        layerlist.append((depth, range_))
    while True:
        severities = []
        for layer in layerlist:
            depth, range_ = layer
            caught = (depth + delay) % (range_ * 2 - 2) == 0
            if caught:
                severities.append(depth * range_)
                break
        if len(severities) == 0:
            return delay
        else:
            delay += 1


if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readlines()
    solution = solve(inp)
    print(solution)
