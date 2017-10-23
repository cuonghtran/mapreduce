#!/usr/bin/python

import sys
from operator import itemgetter


def main():
    current_word = None
    current_count = 0
    word = None

    # input comes from STDIN
    for line in sys.stdin:
        word, count = line.strip().split('\t', 1)

        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            continue

        if current_word == word:
            current_count += count
        else:
            if current_word:
                print(str(current_count) + "\t" + current_word)
            current_count = count
            current_word = word

    if current_word == word:
        print(str(current_count) + "\t" + current_word)


if __name__ == '__main__':
    main()
