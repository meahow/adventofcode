import solution1

"""
For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
"""

def test_isvalid_1():
    p = "aa bb cc dd ee"
    assert solution1.is_valid(p) == True


def test_isvalid_2():
    p = "aa bb cc dd aa"
    assert solution1.is_valid(p) == False


def test_isvalid_3():
    p = "aa bb cc dd aaa"
    assert solution1.is_valid(p) == True


def test_solve():
    data = ("aa bb cc dd ee\n",
            "aa bb cc dd aa\n",
            "aa bb cc dd aaa\n")
    assert solution1.solve(data) == 2

