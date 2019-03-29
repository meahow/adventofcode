import solution2


def test_1():
    testinput = (
        "5 9 2 8\n",
        "9 4 7 3\n",
        "3 8 6 5\n",
    )
    assert solution2.solve(testinput) == 9
