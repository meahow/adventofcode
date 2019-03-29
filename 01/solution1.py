# python

with open('input.txt') as infile:
    current_frequency = 0
    for line in infile.readlines():
        current_frequency += int(line)

print(current_frequency)