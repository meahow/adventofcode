import solution1

"""
For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).
"""

def test_1():
    steps = "ne,ne,ne"
    assert solution1.solve(steps) == 3

def test_2():
    steps = "ne,ne,sw,sw"
    assert solution1.solve(steps) == 0

def test_3():
    steps = "ne,ne,s,s"
    assert solution1.solve(steps) == 2

def test_4():
    steps = "se,sw,se,sw,sw"
    assert solution1.solve(steps) == 3

