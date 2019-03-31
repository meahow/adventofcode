# python3


def solve(blocks):
    counter = 0
    configs = set()
    num_blocks = len(blocks)
    while True:
        current_config = "_".join(map(str, blocks))
        if current_config in configs:
            return counter
        else:
            configs.add(current_config)
        picked_block = blocks.index(max(blocks))
        to_redistribute = blocks[picked_block]
        blocks[picked_block] = 0
        for i in range(1, to_redistribute + 1):
            idx = (i + picked_block) % num_blocks
            blocks[idx] += 1
        counter += 1

if __name__ == '__main__':
    with open("input.txt") as infile:
        memory_blocks = list(map(int, infile.readline().split()))
    solution = solve(memory_blocks)
    print(solution)
