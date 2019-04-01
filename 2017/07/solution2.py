# python3
from collections import namedtuple, Counter
import re

Node = namedtuple('Node', "ID weight children total_weight")
nodes = dict()

def weigh(node_id, correct_total_weight=0):
    node = nodes[node_id]
    weights = []
    if node.children:
        weights = list(map(weigh, node.children))
        hist = Counter(weights)
        if len(hist) != 1:
            correct = hist.most_common(1)[0][0]
            incorrect = hist.most_common()[1][0]
            incorrect_idx = weights.index(incorrect)
            incorrect_node_id = node.children[incorrect_idx]
            # children differ in weight, pass it on
            return weigh(incorrect_node_id, correct)
        elif correct_total_weight:
            # children don't differ, we have to correct myself
            correct_self_weight = correct_total_weight - sum(weights)
            print(f"correcting self from {node.weight} to {correct_self_weight}")
            return node.weight, correct_self_weight
        else:
            return node.weight + sum(weights)
    else:
        if correct_total_weight:
            print(f"correcting total from {node.weight} to {correct_total_weight}")
            return node.weight, correct_total_weight
        else:
            return node.weight

def solve(lines):
    children_nodes = set()
    for line in lines:
        # "fwft (72) -> ktlj, cntj, xhth"
        match = re.split(r"\W+", line)
        node = Node(match[0], int(match[1]), match[2:-1], 0)
        nodes[node.ID] = node
        children_nodes.update(node.children)
        print(node)
    root = (nodes.keys() - children_nodes).pop()
    print("root: %s" % root)

    return weigh(root)[1]

if __name__ == '__main__':
    with open("input.txt") as infile:
        graph = infile.readlines()
    solution = solve(graph)
    print(solution)
