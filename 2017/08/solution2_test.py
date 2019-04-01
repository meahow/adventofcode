import solution2

"""
To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).
"""

def test_solve():
    testdata = (
            "b inc 5 if a > 1\n",
            "a inc 1 if b < 5\n",
            "c dec -10 if a >= 1\n",
            "c inc -20 if c == 10\n",
            )
    assert solution2.solve(testdata) == 10

