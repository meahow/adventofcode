import solution1

testdata = [
        "0 <-> 2\n",
        "1 <-> 1\n",
        "2 <-> 0, 3, 4\n",
        "3 <-> 2, 4\n",
        "4 <-> 2, 3, 6\n",
        "5 <-> 6\n",
        "6 <-> 4, 5\n",
]

def test_1():
    assert solution1.solve(testdata, 0) == 6

