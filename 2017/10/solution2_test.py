import solution2

"""
Here are some example hashes:

The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.
"""

def test_1():
    input_line = ""
    thelist = list(range(256))
    assert solution2.solve(thelist, input_line) == "a2582a3a0e66e6e86e3812dcb672a272"

def test_2():
    input_line = "AoC 2017"
    thelist = list(range(256))
    assert solution2.solve(thelist, input_line) == "33efeb34ea91902bb2f59c9920caa6cd"

def test_3():
    input_line = "1,2,3"
    thelist = list(range(256))
    assert solution2.solve(thelist, input_line) == "3efbe78a8d82f29979031a4aa0b16a9d"

def test_4():
    input_line = "1,2,4"
    thelist = list(range(256))
    assert solution2.solve(thelist, input_line) == "63960835bcdc130f0b66d7ff4f6a5a8e"

def test_5():
    thelist = list(range(5))
    input_lengths = [3, 4, 1, 5]
    # assert solution2.round(thelist, input_lengths, 1) == [3, 4, 2, 1, 0]
    # 3 4 2 1 [0], pos=4, skip=4, length=3
    # 3 0 [2] 1 4, pos=2, skip=5, lenght=4
    # 2 [0] 3 4 1, pos=1, skip=6, length=1
    # 2 0 3 [4] 1, pos=3, skip=7, length=5
    # 2 1 4 3 0, pos=, skip=8, 
    assert solution2.round(thelist, input_lengths, 2) == [2, 1, 4, 3, 0]

def test_round_1():
    input_line = [2]
    thelist = list(range(5))
    assert solution2.round(thelist, input_line, 1) == [1, 0]

def test_round_2():
    input_line = [2]
    thelist = list(range(5))
    assert solution2.round(thelist, input_line, 10) == [0, 1]
