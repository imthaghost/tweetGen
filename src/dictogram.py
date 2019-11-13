#!python
import os
import re  # regular expression library
import time
import logging
from decimal import *
#from wrapper import time_it
#from threading import Threads
#from multiprocessing import Process
from random import random, choice, uniform, randint


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, wordlist=None, path=None):
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
        if path:
            some_words = self.get_words(path)
            for word in some_words:
                if word:
                    self[word] = self.get(word, 0) + 1
        if wordlist:
            for word in wordlist:
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

    def sample(self, num=1):
        v = VoseAlias(self)
        return v.sample_n(num)


class VoseAlias(object):
    """ A probability distribution for discrete weighted random variables and its probability/alias
    tables for efficient sampling via Vose's Alias Method (a good explanation of which can be found at
    http://www.keithschwarz.com/darts-dice-coins/).
    """

    def __init__(self, dist):
        """Given a definition try matching a word to the definition :)

        Parameters
        ----------
        key : str
            Your dictionary.com api key
        wordlist : str
            Path to any wordlist you want by default it uses the OSX built in word list
        Raises
        ------
        TypeError
            If the randomly generated word is not found on dictionary.com
        """
        self.dist = dist
        self.alias_initialisation()
        self.table_prob_list = list(self.table_prob)

    def alias_initialisation(self):
        """Given a definition try matching a word to the definition :)

        Parameters
        ----------
        key : str
            Your dictionary.com api key
        wordlist : str
            Path to any wordlist you want by default it uses the OSX built in word list
        Raises
        ------
        TypeError
            If the randomly generated word is not found on dictionary.com
        """
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
        """Given a definition try matching a word to the definition :)

        Parameters
        ----------
        key : str
            Your dictionary.com api key
        wordlist : str
            Path to any wordlist you want by default it uses the OSX built in word list
        Raises
        ------
        TypeError
            If the randomly generated word is not found on dictionary.com
        """
        # Determine which column of table_prob to inspect
        col = choice(self.table_prob_list)

        # Determine which outcome to pick in that column
        if self.table_prob[col] >= uniform(0, 1):
            return col
        else:
            return self.table_alias[col]

    def sample_n(self, size):
        """Given a definition try matching a word to the definition :)

        Parameters
        ----------
        key : str
            Your dictionary.com api key
        wordlist : str
            Path to any wordlist you want by default it uses the OSX built in word list
        Raises
        ------
        TypeError
            If the randomly generated word is not found on dictionary.com
        """
        # Ensure a non-negative integer as been specified
        n = int(size)
        if n <= 0:
            raise ValueError(
                "Please enter a non-negative integer for the number of samples desired: %d" % n)

        return [self.alias_generation() for i in range(n)]


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(wordlist=word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    sample_list = []
    for x in range(10000):
        sample_list.append(histogram.sample())
    samples = []
    for arrs in sample_list:
        samples.append(arrs[0])
    samples_hist = Dictogram(wordlist=samples)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(
            error) < 0.1 else red
        print('| {!r:<9} '.format(word)
              + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
                + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
                + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    pass

    # histogram = Dictogram(path='thus.txt')
    # print(type(dict(histogram)))
    # print(histogram.sample(10))
    # fish_words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    # print_histogram(fish_words)


if __name__ == '__main__':
    main()
