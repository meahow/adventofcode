# python3


def solve(graphtxt):
    nodes = dict()
    for line in graphtxt:
        line = line.split()
        nodeid = int(line[0])
        children = list(map(lambda s: int(s.strip(',')), line[2:]))
        nodes[nodeid] = children
    visited = set()
    numgroups = 0
    for node in nodes.keys():
        if node in visited:
            continue
        numgroups += 1
        nodes_to_process = [node]
        while nodes_to_process:
            current_node = nodes_to_process.pop()
            if current_node in visited:
                continue
            visited.add(current_node)
            nodes_to_process.extend(nodes[current_node])
    return numgroups

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readlines()
    solution = solve(inp)
    print(solution)
