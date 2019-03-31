import solution2

"""
For example, consider the following list of jump offsets:

0
3
0
1
-3
"""

def test_solve():
    data = [
            0 ,
            3 ,
            0 ,
            1 ,
            -3,
            ]
    assert solution2.solve(data) == 10

