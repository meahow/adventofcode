# python3


def solve(thelist, skiplist):
    # convert chars to ascii numbers
    asciiskiplist = [ord(c) for c in skiplist]
    asciiskiplist.extend([17, 31, 73, 47, 23])
    # calculate dense hash
    thelist = round(thelist, asciiskiplist)
    # calculate sparse hash (XOR)
    assert len(thelist) == 256
    outputlist = []
    for i in range(0, 255, 16):
        currentslice = thelist[i:i + 16]
        xor = 0
        for j in currentslice:
            xor ^= j
        outputlist.append(xor)
    # make a hex
    return "".join(["%x" % x for x in outputlist])

def round(thelist, skiplist):
    lenlist = len(thelist)
    idx = 0
    skip = 0
    lenskiplist = len(skiplist)
    for round in range(64):
        # print("starting round ", round)
        # print("thelist: ", thelist)
        for skip in range(skip, skip + lenskiplist):
            length = skiplist[skip % lenskiplist]
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
    return thelist

if __name__ == '__main__':
    with open("input.txt") as infile:
        inp = infile.readline()
    thelist = list(range(256))
    solution = solve(thelist, inp)
    print(solution)
