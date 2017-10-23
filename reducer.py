#!/usr/bin/python

import sys
import collections


def main():
    current_word = None
    current_count = 0
    word = None
    top_counter = collections.Counter()

    for line in sys.stdin:
        # parse the input we got from mapper.py
        word, count = line.strip().split('\t', 1)

        # counting
        top_counter[word] += int(count)

        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            continue

        if current_word == word:
            current_count += count
        else:
            # if current_word:
            #     print(str(current_count) + "\t" + current_word)
            current_count = count
            current_word = word

    # if current_word == word:
    #     print(str(current_count) + "\t" + current_word)

    for con in top_counter.most_common(100):
        print(str(con[1]) + "\t" + str(con[0]))


if __name__ == '__main__':
    main()
