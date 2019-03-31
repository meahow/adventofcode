# python3


def solve(lines):
    nodes = set()
    children_nodes = set()
    for line in lines:
        # "fwft (72) -> ktlj, cntj, xhth"
        parts = line.split()
        node_id = parts[0]
        nodes.add(node_id)
        if len(parts) > 3:
            children_ids = tuple(map(lambda s: s.strip(','), parts[3:]))
            children_nodes.update(children_ids)
    root = nodes - children_nodes
    assert len(root) == 1
    return root.pop()

if __name__ == '__main__':
    with open("input.txt") as infile:
        graph = infile.readlines()
    solution = solve(graph)
    print(solution)
