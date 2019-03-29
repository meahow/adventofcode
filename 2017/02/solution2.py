# python3


def solve(lines):
    the_sum = 0
    for line in lines:
        numbers = list(map(int, line.split()))
        division = 0
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if (numbers[i] % numbers[j]) == 0:
                    division = int(numbers[i] / numbers[j])
                    break
                elif (numbers[j] % numbers[i]) == 0:
                    division = int(numbers[j] / numbers[i])
                    break
            if division:
                the_sum += division
                break
    return the_sum


if __name__ == '__main__':
    with open('input.txt') as infile:
        solution = solve(infile.readlines())
    print(solution)
