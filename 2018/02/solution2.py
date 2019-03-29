# python3


def str_distance(s1, s2):
    distance = 0
    common = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
        else:
            common.append(s1[i])
    return distance, "".join(common)


with open('input1.txt') as infile:
    box_ids = set()
    for box_id in infile.readlines():
        box_hist = dict()
        for letter in box_id:
            if letter not in box_hist:
                box_hist[letter] = 1
            else:
                box_hist[letter] += 1
        if 2 in box_hist.values() or 3 in box_hist.values():
            box_ids.add(box_id[:-1])  # cut the trailing newline

print("box IDs count: %d" % len(box_ids))
box_ids = list(box_ids)

for i in range(len(box_ids) - 1):
    for j in range(i + 1, len(box_ids)):
        # print(f"comparing IDs {i} and {j}")
        box_id1 = box_ids[i]
        box_id2 = box_ids[j]
        distance, common_str = str_distance(box_id1, box_id2)
        # print(f"str_distance({box_id1}, {box_id2}) = {str_distance(box_id1, box_id2)}")
        if distance == 1:
            print("Found correct box IDs: %s, %s"
                  % (box_id1, box_id2))
            print("common string between them: %s" % common_str)
