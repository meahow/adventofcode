# python3
from collections import Counter

def is_valid(passphrase):
    words = passphrase.split()
    seen_words = list()
    for word in words:
        hist = Counter(word)
        if hist in seen_words:
            return False
        seen_words.append(hist)
    return True


def solve(passphrases):
    valids = [1 for s in passphrases if is_valid(s.strip()) ]
    return len(valids)

if __name__ == '__main__':
    with open("input.txt") as infile:
        solution = solve(infile.readlines())
    print(solution)
