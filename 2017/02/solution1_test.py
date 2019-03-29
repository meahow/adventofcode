import solution1


def test_1():
    testinput = ["5 1 9 5\n", "7 5 3\n", "2 4 6 8\n"]
    assert solution1.solve(testinput) == 18
