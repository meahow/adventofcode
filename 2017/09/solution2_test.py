import solution2

"""
<>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.
"""

def test_1():
    testdata = "<>"
    assert solution2.solve(testdata) == 0

def test_2():
    testdata = "<random characters>"
    assert solution2.solve(testdata) == 17

def test_3():
    testdata = "<<<<>"
    assert solution2.solve(testdata) == 3

def test_4():
    testdata = "<{!>}>"
    assert solution2.solve(testdata) == 2

def test_5():
    testdata = "<!!>"
    assert solution2.solve(testdata) == 0

def test_6():
    testdata = "<!!!>>"
    assert solution2.solve(testdata) == 0

def test_7():
    testdata = '<{o"i!a,<{i<a>'
    assert solution2.solve(testdata) == 10

def test_8():
    testdata = '{{{{{{{<>},<<!>},<,>},{{<oou<o{!>,<i!!!!!>!!ouu}i>}}}}}}'
    assert solution2.solve(testdata) == 19

def test_9():
    testdata = '{{},{}, <123>, <12!3!>4>}'
    assert solution2.solve(testdata) == 6

