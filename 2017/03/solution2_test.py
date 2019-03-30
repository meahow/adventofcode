import solution2

"""
So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
"""

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, 1)
DOWN = (0, -1)

moves = (
    # layer 1
    RIGHT, UP, LEFT, LEFT,
    DOWN, DOWN, RIGHT, RIGHT,
    # layer 2
    RIGHT,
    UP, UP, UP, 
    LEFT, LEFT, LEFT, LEFT,
    DOWN, DOWN, DOWN, DOWN,
    RIGHT, RIGHT, RIGHT, RIGHT,
    # layer 3
    RIGHT,
    UP, UP, UP, UP, UP,
    LEFT, LEFT, LEFT, LEFT, LEFT, LEFT,
    DOWN, DOWN, DOWN, DOWN, DOWN, DOWN,
    RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT,
    # layer 4
    RIGHT,
    )

def test_coordinates():
    gen = solution2.coordinates()
    assert next(gen) == (0,0)
    assert next(gen) == (1,0)
    assert next(gen) == (1,1)
    assert next(gen) == (0,1)
    assert next(gen) == (-1,1)
    assert next(gen) == (-1,0)
    assert next(gen) == (-1,-1)
    assert next(gen) == (0,-1)
    assert next(gen) == (1,-1)
    assert next(gen) == (2,-1)
    assert next(gen) == (2,0)
    assert next(gen) == (2,1)
    assert next(gen) == (2,2)
    assert next(gen) == (1,2)
    assert next(gen) == (0,2)
    assert next(gen) == (-1,2)
    assert next(gen) == (-2,2)
    assert next(gen) == (-2,1)
    assert next(gen) == (-2,0)
    assert next(gen) == (-2,-1)
    assert next(gen) == (-2,-2)


def test_coordinates_diff():
    gen = solution2.coordinates_diff()
    i = 0
    for move in gen:
        if i >= len(moves):
            return
        print(move)
        assert move == moves[i]
        i += 1


def test_square():
    """
    147  142  133  122   59
    304    5    4    2   57
    330   10    1    1   54
    351   11   23   25   26
    362  747  806--->   ...
    """
    n = solution2.square()
    assert next(n) == 1
    assert next(n) == 1
    assert next(n) == 2
    assert next(n) == 4
    assert next(n) == 5
    assert next(n) == 10
    assert next(n) == 11
    assert next(n) == 23
    assert next(n) == 25
    assert next(n) == 26
    assert next(n) == 54
    assert next(n) == 57
    assert next(n) == 59
    assert next(n) == 122
    assert next(n) == 133
    assert next(n) == 142
    assert next(n) == 147
    assert next(n) == 304
    assert next(n) == 330
    assert next(n) == 351
    assert next(n) == 362
    assert next(n) == 747
    assert next(n) == 806
