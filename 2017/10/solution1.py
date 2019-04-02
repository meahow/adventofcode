# python3


def solve(thelist, lengths):
    assert len(thelist) > len(lengths)
    return thelist[0] * thelist[1]

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readline()
    inp = list(map(int, inp.split(',')))
    thelist = list(range(256))
    solution = solve(thelist, inp)
    print(solution)
