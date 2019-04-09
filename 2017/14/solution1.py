# python3

import knothash

def solve(key):
    grid = []
    bits_used = 0
    for i in range(128):
        thelist = list(range(256))
        current_key = "{}-{}".format(key, i)
        thehash = knothash.solve(thelist, current_key)
        hash_binary = bin(int(thehash, 16))
        bits = hash_binary.count('1')
        bits_used += bits
        grid.append(thehash)
    print(grid)
    return bits_used


if __name__ == '__main__':
    solution = solve('ljoxqyyw')
    print(solution)
