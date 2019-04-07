# python3

moves = {
        "n": (0, 2),
        "s": (0, -2),
        "ne": (1, 1),
        "se": (1, -1),
        "nw": (-1, 1),
        "sw": (-1, -1),
        }

def solve(steps):
    steps = steps.split(",")
    x, y = (0, 0)
    maxsteps = 0
    for step in steps:
        move = moves[step]
        x += move[0]
        y += move[1]
        absx = abs(x)
        absy = abs(y)
        numsteps = min(absx,absy) + abs(absx - absy)//2
        maxsteps = max(maxsteps, numsteps)
    return maxsteps

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readline()
    steps = inp.strip()
    solution = solve(steps)
    print(solution)
