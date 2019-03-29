import solution2


def test_1():
    assert solution2.solve("1212") ==6


def test_2():
    assert solution2.solve("1221") == 0


def test_3():
    assert solution2.solve("123425") == 4


def test_4():
    assert solution2.solve("123123") == 12


def test_5():
    assert solution2.solve("12131415") == 4
