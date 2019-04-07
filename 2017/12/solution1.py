# python3


def solve(graphtxt, node=0):
    nodes = dict()
    for line in graphtxt:
        line = line.split()
        nodeid = int(line[0])
        children = list(map(lambda s: int(s.strip(',')), line[2:]))
        nodes[nodeid] = children
    print(nodes) 
    visited = set()
    nodes_to_process = [node]
    while nodes_to_process:
        current_node = nodes_to_process.pop()
        if current_node in visited:
            continue
        visited.add(current_node)
        nodes_to_process.extend(nodes[current_node])
    return len(visited)

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readlines()
    solution = solve(inp, 0)
    print(solution)
