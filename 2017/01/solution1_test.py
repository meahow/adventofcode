import solution1


def test_1():
    assert solution1.solve("1122") == 3


def test_2():
    assert solution1.solve("1111") == 4


def test_3():
    assert solution1.solve("1234") == 0


def test_4():
    assert solution1.solve("91212129") == 9
