import solution1

"""
{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{},{}}, score of 1 + 2 + 2 = 5.
{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
{<a>,<a>,<a>,<a>}, score of 1.
{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
"""

def test_1():
    testdata = "{}"
    assert solution1.solve(testdata) == 1 

def test_2():
    testdata = "{{{}}}"
    assert solution1.solve(testdata) == 6 

def test_3():
    testdata = "{{},{}}"
    assert solution1.solve(testdata) == 5 

def test_4():
    testdata = "{{{},{},{{}}}}"
    assert solution1.solve(testdata) == 16 

def test_5():
    testdata = "{<a>,<a>,<a>,<a>}"
    assert solution1.solve(testdata) == 1 

def test_6():
    testdata = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
    assert solution1.solve(testdata) == 9 

def test_7():
    testdata = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
    assert solution1.solve(testdata) == 9 

def test_8():
    testdata = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
    assert solution1.solve(testdata) == 3 
