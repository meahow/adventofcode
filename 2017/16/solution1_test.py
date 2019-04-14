import solution1

def test_1():
    testdata = "s1,x3/4,pe/b"
    assert solution1.solve(testdata, 5) == "baedc"

def test_2():
    testdata = "s3"
    assert solution1.solve(testdata, 5) == "cdeab"

