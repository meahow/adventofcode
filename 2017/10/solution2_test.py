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
    assert solution2.solve(thelist, input_line) == "33efeb34ea91902bb2f59c9920caa6cd."

def test_3():
    input_line = "1,2,3"
    thelist = list(range(256))
    assert solution2.solve(thelist, input_line) == "3efbe78a8d82f29979031a4aa0b16a9d."

def test_4():
    input_line = "1,2,4"
    thelist = list(range(256))
    assert solution2.solve(thelist, input_line) == "63960835bcdc130f0b66d7ff4f6a5a8e."

