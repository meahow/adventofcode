# python3

def solve(commands, length=16):
    a = ord('a')
    end = a + length
    letters = [chr(s) for s in range(a, end)]
    for cmd in commands.split(','):
        c = cmd[0]
        if c == 's':
            # spin
            l = int(cmd[1:])
            letters = letters[-l:] + letters[:-l]
        elif c == 'x':
            # exchange
            c1, c2 = list(map(int, cmd[1:].split('/')))
            letters[c2], letters[c1] = letters[c1], letters[c2]
        elif c == 'p':
            # partners
            c1, c2 = cmd[1:].split('/')
            i1 = letters.index(c1)
            i2 = letters.index(c2)
            letters[i2], letters[i1] = letters[i1], letters[i2]
        else:
            raise ValueError("incorrect")

    return "".join(letters)

if __name__ == '__main__':
    with open("input.txt") as f:
        commands = f.readline().strip()
    solution = solve(commands)
    print(solution)
