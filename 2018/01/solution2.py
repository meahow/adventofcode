# python
import sys

with open('input.txt') as infile:
    current_frequency = 0
    freqs_seen = dict()
    lines = infile.readlines()
    loop_counter = 0
    while True:
        loop_counter += 1
        print("Looping for the %d time" % loop_counter)
        print("freq count: %d, freq: %d" %
              (len(freqs_seen), current_frequency))
        for line in lines:
            current_frequency += int(line)
            if current_frequency in freqs_seen:
                print("I've seen frequency of %d twice!" % current_frequency)
                sys.exit()
            freqs_seen[current_frequency] = 1
