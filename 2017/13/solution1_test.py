import solution1

testdata = [
        "0: 3\n",
        "1: 2\n",
        "4: 4\n",
        "6: 4\n",
        ]

def test_1():
    assert solution1.solve(testdata) == 24

