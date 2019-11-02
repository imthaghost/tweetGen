import os
import random
import time
import re
import sys
from decimal import *
from optparse import OptionParser


def time_it(func):
    """

    """
    def wrapper(*args, **kwargs):
        """Returns random words from a file 

        Parameters
        ----------
        path : str, OSX words list by default
            The path of the words file

        num : int, at least 1 word by default
            The number of words we want to return

        Raises
        ------
        TypeError
            If no no or 1 parameter was given...requires two keyword parameters path and ammount
        """
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " ms")
        return result

    return wrapper


class VoseAlias(object):
    """ A probability distribution for discrete weighted random variables and its probability/alias
    tables for efficient sampling via Vose's Alias Method (a good explanation of which can be found at
    http://www.keithschwarz.com/darts-dice-coins/).
    """

    def __init__(self, dist):
        """ (VoseAlias, dict) -> NoneType """
        self.dist = dist
        self.alias_initialisation()
        self.table_prob_list = list(self.table_prob)

    def alias_initialisation(self):
        """ Construct probability and alias tables for the distribution. """
        # Initialise variables
        n = len(self.dist)
        self.table_prob = {}   # probability table
        self.table_alias = {}  # alias table
        scaled_prob = {}       # scaled probabilities
        small = []             # stack for probabilities smaller that 1
        large = []             # stack for probabilities greater than or equal to 1

        # Construct and sort the scaled probabilities into their appropriate stacks
        for o, p in self.dist.items():
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
        col = random.choice(self.table_prob_list)

        # Determine which outcome to pick in that column
        if self.table_prob[col] >= random.uniform(0, 1):
            return col
        else:
            return self.table_alias[col]

    @time_it
    def sample_n(self, size):
        """ Return a sample of size n from the distribution."""
        # Ensure a non-negative integer as been specified
        n = int(size)
        if n <= 0:
            raise ValueError(
                "Please enter a non-negative integer for the number of samples desired: %d" % n)

        return [self.alias_generation() for i in range(n)]


# HELPER FUNCTIONS
def get_words(file):
    """ (str) -> list
    Return a list of words from a given corpus. """

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
            raise IOError("Please provide a file containing text-based data.")

    with open(file, "r") as corpus:
        words = corpus.read().lower()
        words_list = re.sub(r'[^a-zA-Z\s]', '', words).split()
    return words_list


@time_it
def sample2dist(sample):
    """ (list) -> dict (i.e {outcome:proportion})
    Construct a distribution based on an observed sample (e.g. rolls of a bias die) """
    increment = Decimal(1)/len(sample)

    dist = {}
    get = dist.get
    for o in sample:  # o for outcome
        dist[o] = get(o, 0) + increment

    return dist

# def main():
#     # Handle command line arguments
#     # options = handle_options()

#     try:
#         # Construct distribution
#         words = get_words(options.path)
#         word_dist = sample2dist(words)
#         VA_words = VoseAlias(word_dist)

#         # Sample n words
#         print("\nGenerating %d random samples:\n" % options.n)
#         sample = VA_words.sample_n(options.n)
#         for s in sample:
#             print(s)
#     except Exception as e:
#         sys.exit("\nError: %s" % e)


# if __name__ == "__main__":
#     words = get_words('/usr/share/dict/words')
#     histogram = sample2dist(words)
#     VA = VoseAlias(histogram)
#     print(VA.sample_n(size=100))
