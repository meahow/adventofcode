# python3


def solve(jumps):
    counter = 0
    ip = 0
    try:
        while True:
            jmp = jumps[ip]
            jumps[ip] += 1
            ip += jmp
            counter += 1
    except IndexError:
        return counter

if __name__ == '__main__':
    with open("input.txt") as infile:
        jumps = map(lambda s: int(s.strip()), infile.readlines())
    solution = solve(jumps)
    print(solution)
