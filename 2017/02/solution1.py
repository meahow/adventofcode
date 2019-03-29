# python3


def solve(lines):
    the_sum = 0
    for line in lines:
        numbers = list(map(int, line.split()))
        the_sum += (max(numbers) - min(numbers))
    return the_sum


if __name__ == '__main__':
    with open('input.txt') as infile:
        solution = solve(infile.readlines())
    print(solution)
