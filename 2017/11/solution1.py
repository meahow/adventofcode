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
    position = move(steps)
    print(position)
    x, y = [abs(x) for x in position]
    numsteps = min(x,y) + abs(x - y)//2
    return numsteps

def move(steps):
    steps = steps.split(",")
    x, y = (0, 0)
    for step in steps:
        move = moves[step]
        x += move[0]
        y += move[1]
    return (x,y)

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readline()
    steps = inp.strip()
    solution = solve(steps)
    print(solution)
