# python3
from collections import namedtuple

Claim = namedtuple('Claim', ['ID', 'x', 'y', 'width', 'height'])


def parseInput(filename='input.txt'):
    claims = dict()
    with open(filename) as infile:
        for i in infile.readlines():
            line = i.strip()
            # ;ine format: "#123 @ 3,2: 5x4"
            id_, _, start, size = line.split()
            id_ = int(id_[1:])
            x, y = map(int, start[:-1].split(','))
            width, height = map(int, size.split('x'))

            claim = Claim(id_, x, y, width, height)
            claims[id_] = claim
    return claims


claims = parseInput()
print(claims)
