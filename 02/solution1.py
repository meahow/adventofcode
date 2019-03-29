# python3

with open('input1.txt') as infile:
    num_twos = 0
    num_threes = 0
    for box_id in infile.readlines():
        box_hist = dict()
        for letter in box_id:
            if letter not in box_hist:
                box_hist[letter] = 1
            else:
                box_hist[letter] += 1
        if 2 in box_hist.values():
            num_twos += 1
        if 3 in box_hist.values():
            num_threes += 1

print(f"twos: {num_twos}, threes: {num_threes}\n",
      f"checksum: {num_twos*num_threes}")
