# python3

def solve(seed1, seed2):
    genA = gen(seed1, 16807, 4)
    genB = gen(seed2, 48271, 8)
    pairs = zip(genA, genB)
    counter = 0
    i = 0
    for x, y in pairs:
        i += 1
        if x == y:
            counter += 1
            print(counter, "match!")
            print("{}\n{:016b}\n{:016b}".format(i, x, y))
    return counter

def gen(seed, factor, denominator):
    current = seed
    i = 0
    while i < 5000000:
        current *= factor
        current %= 2147483647
        if current % denominator == 0:
            i += 1
            yield current % 65536

if __name__ == '__main__':
    solution = solve(883, 879)
    print(solution)
