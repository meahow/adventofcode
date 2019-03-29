# python3


def solve(captcha):
    # add 'circularity'
    the_sum = 0
    half = len(captcha) // 2
    captcha = captcha + captcha[:half]
    for i in range(len(captcha) - half):
        if captcha[i] == captcha[i + half]:
            the_sum += int(captcha[i])
    return the_sum


if __name__ == '__main__':
    with open('input.txt') as infile:
        solution = solve(infile.readline().strip())
    print(solution)
