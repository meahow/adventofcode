import solution1

"""
For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
"""

def test_1():
    assert solution1.solve(1) == 0


def test_12():
    assert solution1.solve(12) == 3


def test_23():
    assert solution1.solve(23) == 2


def test_1024():
    assert solution1.solve(1024) == 31


def test_layers_1():
    assert solution1.layers(1) == (1,1)


def test_layers_2():
    for i in range(2, 10):
        assert solution1.layers(i) == (2,i-1)


def test_layers_3():
    for i in range(10, 26):
        assert solution1.layers(i) == (3,i - 9)


def test_layers_4():
    for i in range(26, 50):
        assert solution1.layers(i) == (4,i - 25)


def test_layers_5():
    for i in range(50, 82):
        assert solution1.layers(i) == (5,i - 49)


def test_layers_6():
    for i in range(82, 122):
        assert solution1.layers(i) == (6,i - 81)

def test_numelems():
    n = solution1.num_elems()
    assert next(n) == (1, 1)
    assert next(n) == (2, 8)
    assert next(n) == (3, 16)
    assert next(n) == (4, 24)
    assert next(n) == (5, 32)
    assert next(n) == (6, 40)
    assert next(n) == (7, 48)
    assert next(n) == (8, 56)
    assert next(n) == (9, 64)
    assert next(n) == (10, 72)
    assert next(n) == (11, 80)
