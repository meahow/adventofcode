# python3

def is_valid(passphrase):
    words = passphrase.split()
    seen_words = set()
    for word in words:
        if word in seen_words:
            return False
        seen_words.add(word)
    return True


def solve(passphrases):
    valids = [1 for s in passphrases if is_valid(s.strip()) ]
    return len(valids)

if __name__ == '__main__':
    with open("input.txt") as infile:
        solution = solve(infile.readlines())
    print(solution)
