#!python
import os
import re  # regular expression library
from decimal import *
from random import random, choice, uniform
from dictionary_words import time_it
import logging
from vose import VoseAlias, sample2dist


# from __future__ import division, print_function  # Python 2 and 3 compatibility


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, path=None):
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
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        self.word_count = 0  # word count
        # self.table_prob_list = list(self.table_prob)
        if path is not None:
            some_words = []
            # open the text file
            with open(path, 'r') as f:
                # convert all words to lowecase to catch exceptions and edge cases
                words = f.read().lower()
                # create a words list
                words_list = re.sub(r'[^a-zA-Z\s]', '', words)
                # reassign the list
                some_words = words_list.split()
                # set the amount of words in the list to the instance variable token
                self.token = len(some_words)
            # find all words
            for word in some_words:
                if word:
                    self[word] = self.get(word, 0) + 1
        # after creating key-value pairs create instance variable that contains the sum of all values
        self.sum = sum([self.get(key, 0) for key in self])  # sum of weights
        self.alias_initialisation()  # wtf
        self.table_prob_list = list(self.table_prob)  # still not sure

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

    # def alias_generation(self):
    #     """ Return a random outcome from the distribution. """
    #     # Determine which column of table_prob to inspect
    #     col = choice(self.table_prob_list)

    #     # Determine which outcome to pick in that column
    #     if self.table_prob[col] >= uniform(0, 1):
    #         return col
    #     else:
    #         return self.table_alias[col]

    # def sample_n(self, size):
    #     """ Return a sample of size n from the distribution."""
    #     # Ensure a non-negative integer as been specified
    #     n = int(size)
    #     if n <= 0:
    #         raise ValueError(
    #             "Please enter a non-negative integer for the number of samples desired: %d" % n)

    #     return [self.alias_generation() for i in range(n)]

    # HELPER FUNCTIONS

    # def get_words(self, file):
    #     """ (str) -> list
    #     Return a list of words from a given corpus. """

    #     # Ensure the file is not empty
    #     if os.stat(file).st_size == 0:
    #         raise IOError(
    #             "Please provide a file containing a corpus (not an empty file).")

    #     # Ensure the file is text based (not binary). This is based on the implementation
    #     #  of the Linux file command
    #     textchars = bytearray([7, 8, 9, 10, 12, 13, 27]) + \
    #         bytearray(range(0x20, 0x100))
    #     with open(file, "rb") as bin_file:
    #         if bool(bin_file.read(2048).translate(None, textchars)):
    #             raise IOError(
    #                 "Please provide a file containing text-based data.")

    #     with open(file, "r") as corpus:
    #         words = corpus.read().split()
    #     return words

    # def sample2dist(self, sample):
    #     """ (list) -> dict (i.e {outcome:proportion})
    #     Construct a distribution based on an observed sample (e.g. rolls of a bias die) """
    #     increment = Decimal(1)/len(sample)

    #     dist = {}
    #     get = dist.get
    #     for o in sample:  # o for outcome
    #         dist[o] = get(o, 0) + increment
    #     return dist

    def sample_it(self):
        sample2dist(self)

    @time_it
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
        word = word.lower()
        return self.get(word, 0)

    def get_val(self, key):
        return self[key]

    def prob(self, key):
        x = self.get_val(key) / self.sum
        return x


# def print_histogram(word_list):
#     print('word list: {}'.format(word_list))
#     # Create a dictogram and display its contents
#     histogram = Dictogram(word_list)
#     print('dictogram: {}'.format(histogram))
#     print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
#     for word in word_list[-2:]:
#         freq = histogram.frequency(word)
#         print('{!r} occurs {} times'.format(word, freq))
#     print()


def main():
    histogram = Dictogram('/usr/share/dict/words')
    print(histogram.sample_it())


if __name__ == '__main__':
    main()
