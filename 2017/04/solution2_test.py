from collections import Counter
import solution2

"""
For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
"""

def test_isvalid_1():
    p = "abcde fghij"
    assert solution2.is_valid(p) == True

def test_isvalid_2():
    p = "abcde xyz ecdab"
    assert solution2.is_valid(p) == False

def test_isvalid_3():
    p = "a ab abc abd abf abj"
    assert solution2.is_valid(p) == True

def test_isvalid_4():
    p = "iiii oiii ooii oooi oooo"
    assert solution2.is_valid(p) == True

def test_isvalid_5():
    p = "oiii ioii iioi iiio"
    assert solution2.is_valid(p) == False

def test_solve():
    data = (
            "abcde fghij\n",
            "abcde xyz ecdab\n",
            "a ab abc abd abf abj\n",
            "iiii oiii ooii oooi oooo\n",
            "oiii ioii iioi iiio\n",
            )
    assert solution2.solve(data) == 3

