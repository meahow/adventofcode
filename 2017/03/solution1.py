# python3

def num_elems():
    level = 1
    yield level, 1
    while True:
        level += 1
        yield level, 8 * (level - 1)

def layers(num, gen=None):
    if not gen:
        gen = num_elems()
    level, numelems = next(gen)
    #print("layers({}, {})".format(num,  level))
    if num <= 0: raise ValueError()
    remainder = num - numelems
    #print("remainder = %d" % remainder)
    if remainder <= 0:
        return level, num
    else:
        return layers(remainder, gen)

def solve(num):
    if num == 1:
        return 0
    steps = 0
    layer, pos_in_layer = layers(num)
    side_length = (layer - 1) * 2
    pos_on_side = pos_in_layer % side_length
    middle_offset = layer - 1
    steps_on_side = abs(pos_on_side - middle_offset)
    steps_through_layers = layer - 1
    return steps_through_layers + steps_on_side


if __name__ == '__main__':
    solution = solve(325489)
    print(solution)
