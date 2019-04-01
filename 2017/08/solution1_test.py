import solution1

"""
The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.
"""

def test_solve():
    testdata = (
            "b inc 5 if a > 1\n",
            "a inc 1 if b < 5\n",
            "c dec -10 if a >= 1\n",
            "c inc -20 if c == 10\n",
            )
    assert solution1.solve(testdata) == 1

