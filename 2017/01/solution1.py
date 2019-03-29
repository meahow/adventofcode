# python3


def solve(captcha):
    # add 'circularity'
    captcha = captcha + captcha[0]
    the_sum = 0
    for i in range(len(captcha) - 1):
        if captcha[i] == captcha[i + 1]:
            the_sum += int(captcha[i])
    return the_sum


if __name__ == '__main__':
    with open('input.txt') as infile:
        solution = solve(infile.readline().strip())
    print(solution)
