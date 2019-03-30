# python3
from itertools import count

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def sum_tuples(t1, t2):
    return tuple(map(
            lambda x, y: x+y,
            t1, t2)
        )

def coordinates_diff():
    moves = ( (RIGHT, UP),
              (LEFT, DOWN) )
    for num_moves in count(1):
        idx = (num_moves - 1) % 2
        for move in moves[idx]:
            for i in range(num_moves):
                yield move

def coordinates():
    pos = (0, 0)
    for move in coordinates_diff():
        yield pos
        pos = sum_tuples(pos, move)

def square():
    square_dict = dict()
    square_dict[(0,0)] = 1
    neighbour_diffs =  \
        (UP, DOWN, LEFT, RIGHT,
        sum_tuples(UP,LEFT),
        sum_tuples(UP, RIGHT),
        sum_tuples(DOWN, LEFT),
        sum_tuples(DOWN, RIGHT)
        )
    for key in coordinates():
        if key not in square_dict:
            neighbours = []
            for x in neighbour_diffs:
                neigh_key = sum_tuples(key,x)
                neighbour = square_dict.get(neigh_key, 0)
                neighbours.append(neighbour)
            val = sum(neighbours)
            square_dict[key] = val
        yield square_dict[key]
        

    
def solve(num):
    squarrgen = square()
    i = 0
    while i <= num:
        i = next(squarrgen)
        print(i)
    return i


if __name__ == '__main__':
    solution = solve(325489)
    print(solution)

