import solution2

"""
For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

...then you would be able to recreate the structure of the towers that looks like this:

                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth
In this example, tknk is at the bottom of the tower
"""

def test_solve():
    testdata = (
    "pbga (66)\n",
    "xhth (57)\n",
    "ebii (61)\n",
    "havc (66)\n",
    "ktlj (57)\n",
    "fwft (72) -> ktlj, cntj, xhth\n",
    "qoyq (66)\n",
    "padx (45) -> pbga, havc, qoyq\n",
    "tknk (41) -> ugml, padx, fwft\n",
    "jptl (61)\n",
    "ugml (68) -> gyxo, ebii, jptl\n",
    "gyxo (61)\n",
    "cntj (57)\n",)
    assert solution2.solve(testdata) == 60

