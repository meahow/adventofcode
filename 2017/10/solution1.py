# python3


def solve(thelist, skiplist):
    lenlist = len(thelist)
    idx = 0
    for skip in range(len(skiplist)):
        length = skiplist[skip]
        stop = idx + length
        rest = -1
        current_list = thelist[idx:stop]
        if stop > lenlist:
            rest = stop - lenlist
            current_list.extend(thelist[:rest])
        current_list.reverse()
        # update all items
        for i in range(length):
            tmp_idx = (i + idx) % lenlist
            thelist[tmp_idx] = current_list[i]
        jump = length + skip
        idx += jump
        idx %= lenlist
    return thelist[0] * thelist[1]

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readline()
    inp = list(map(int, inp.split(',')))
    thelist = list(range(256))
    solution = solve(thelist, inp)
    print(solution)
