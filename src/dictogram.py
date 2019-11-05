#!python
import os
import re  # regular expression library
import logging
from decimal import *
from random import random, choice, uniform


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, wordlist, path=None):
        """ Initialize this histogram as a new dict and count given words.
            returns a histogram data structure that stores each unique word along with
            the number of times that the word appears in the source text

        Parameters
        ----------
        path : str,
            path to file that contains text you want to create a histogram for

        Returns
        ----------
        Dictogram: dict,
            key value pair - (the unique words and amount of times the word appears)

        Raises
        ------
        TypeError
            If ....
        """
        super().__init__()  # Initialize this as a new dict
        if path is not None:
            some_words = self.get_words(path)
            for word in some_words:
                if word:
                    self[word] = self.get(word, 0) + 1
        else:
            for word in wordlist:
                if word:
                    self[word] = self.get(word, 0) + 1
        # after creating key-value pairs create instance variable that contains the sum of all values
        self.sum = sum([self.get(key, 0) for key in self])  # sum of weights
        # set the amount of words in the list to the instance variable token
        # Count of distinct word types in this histogram
        self.types = len(self)
        self.tokens = sum(self.values())

    def frequency(self, word):
        """returns the frequency in which a word is seen

            Parameters
            ----------
            path : word,

            Returns
            ----------
            historgram: dict,
                key value pair - (the unique words and amount of times the word appears)
        """
        if word in self.keys():
            return self[word]
        else:
            return 0

    def __contains__(self, target):
        return True if target in self.keys() else False

    def add_count(self, word, count=1):
        self.tokens += count
        self[word] = self.get(word, 0) + count
        self.types = len(self)

    def get_words(self, file):
        """ file byte stream -> list
        Return a list of words from a file. """
        # Ensure the file is not empty
        if os.stat(file).st_size == 0:
            raise IOError(
                "Please provide a file containing a corpus (not an empty file).")
        # Ensure the file is text based (not binary). This is based on the implementation
        #  of the Linux file command
        textchars = bytearray([7, 8, 9, 10, 12, 13, 27]) + \
            bytearray(range(0x20, 0x100))
        with open(file, "rb") as bin_file:
            if bool(bin_file.read(2048).translate(None, textchars)):
                raise IOError(
                    "Please provide a file containing text-based data.")
        with open(file, "r") as corpus:
            words = corpus.read().lower()
            words_list = re.sub(r'[^a-zA-Z\s]', '', words).split()
        return words_list

    def alias_initialisation(self):
        """ Construct probability and alias tables for the distribution. """
        # Initialise variables
        n = len(self)
        self.table_prob = {}   # probability table
        self.table_alias = {}  # alias table
        scaled_prob = {}       # scaled probabilities
        small = []             # stack for probabilities smaller that 1
        large = []             # stack for probabilities greater than or equal to 1

        # Construct and sort the scaled probabilities into their appropriate stacks
        for o, p in self.items():
            scaled_prob[o] = Decimal(p) * n

            if scaled_prob[o] < 1:
                small.append(o)
            else:
                large.append(o)

        # Construct the probability and alias tables
        while small and large:
            s = small.pop()
            l = large.pop()

            self.table_prob[s] = scaled_prob[s]
            self.table_alias[s] = l

            scaled_prob[l] = (scaled_prob[l] + scaled_prob[s]) - Decimal(1)

            if scaled_prob[l] < 1:
                small.append(l)
            else:
                large.append(l)

        # The remaining outcomes (of one stack) must have probability 1
        while large:
            self.table_prob[large.pop()] = Decimal(1)

        while small:
            self.table_prob[small.pop()] = Decimal(1)

    def alias_generation(self):
        """ Return a random outcome from the distribution. """
        # Determine which column of table_prob to inspect
        col = choice(self.table_prob_list)

        # Determine which outcome to pick in that column
        if self.table_prob[col] >= uniform(0, 1):
            return col
        else:
            return self.table_alias[col]

    def sample_n(self, size):
        """ Return a sample of size n from the distribution."""
        # Ensure a non-negative integer as been specified
        n = int(size)
        if n <= 0:
            raise ValueError(
                "Please enter a non-negative integer for the number of samples desired: %d" % n)

        return [self.alias_generation() for i in range(n)]

    def sample2dist(self, sample):
        """ (list) -> dict (i.e {outcome:proportion})
        Construct a distribution based on an observed sample (e.g. rolls of a bias die) """
        increment = Decimal(1)/len(sample)

        dist = {}
        get = dist.get
        for o in sample:  # o for outcome
            dist[o] = get(o, 0) + increment
        return dist


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))


def main():
    fish_words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    histogram = Dictogram(fish_words)
    print(histogram)
    print(type(dict(histogram)))


if __name__ == '__main__':
    main()
