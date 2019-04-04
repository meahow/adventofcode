# python3


def solve(steps):
    steps = steps.split(",")
    position = (0, 0)
    moves = {
            "n": (0, 2),
            "s": (0, -2),
            "ne": (1, 1),
            "se": (1, -1),
            "nw": (-1, 1),
            "sw": (-1, -1),
            }
    for step in steps:
        move = moves[step]
        position = zip(position, move)
    print(position)
    return 0

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readline()
    steps = inp.strip()
    solution = solve(steps)
    print(solution)
