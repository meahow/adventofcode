# python3

import knothash

def solve(key):
    grid = []
    print("")
    for i in range(128):
        thelist = list(range(256))
        current_key = "{}-{}".format(key, i)
        thehash = knothash.solve(thelist, current_key)
        binhash = "{:0128b}".format(int(thehash, 16))
        print(binhash)
        grid.append(binhash)
    groups_used = 0
    visited = list()
    for i in range(128):
        empty = list(128 * (0,))
        visited.append(empty)
    queue = list()
    # bfs through all bits
    for x in range(len(grid)):
        line = grid[x]
        for y in range(len(line)):
            bit = line[y]
            if visited[x][y]:
                continue
            elif bit == '1':
                groups_used += 1
                queue.append((x,y))
                while queue:
                    innerx, innery = queue.pop()
                    if visited[innerx][innery]:
                        continue
                    visited[innerx][innery] = groups_used
                    if innerx < 127 and grid[innerx+1][innery] == '1':
                        queue.append((innerx+1,innery))
                    if innerx > 0 and grid[innerx-1][innery] == '1':
                        queue.append((innerx-1,innery))
                    if innery < 127 and grid[innerx][innery+1] == '1':
                        queue.append((innerx,innery+1))
                    if innery > 0 and grid[innerx][innery-1] == '1':
                        queue.append((innerx,innery-1))
    for i in visited:
        s = "|".join(map(str, i))
        print(s)
    return groups_used


if __name__ == '__main__':
    solution = solve('ljoxqyyw')
    print(solution)
