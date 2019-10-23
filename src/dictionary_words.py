import os
from sys import argv
import time
from random import choice


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


@time_it  # benchmark
def dictionary(path='/usr/share/dict/words', num=1):
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
    with open(path, "r") as yeet:
        words = yeet.read().split('\n')
        rand_word = []
        for i in range(int(num)):
            rand_word.append(choice(words))
        return ' '.join(rand_word).capitalize() + '.'

#!################################## Generator ############################


@time_it
def anagram_gen(word):
    if len(word) <= 1:
        yield word
    else:
        for perm in anagram(word[1:]):
            for i in range(len(word)):
                yield perm[:i] + word[0:1] + perm[i:]

#!################################## Generator ############################


@time_it
def anagram(word):
    """Returns random words from a file 

        Parameters
        ----------
        word : str
            Word in which we will return all permutations of

        Raises
        ------
        TypeError
            If no no or 1 parameter was given...requires two keyword parameters path and ammount
        """
    if len(word) <= 1:
        return word
    else:
        tmp = []
        for perm in anagram(word[1:]):
            for i in range(len(word)):
                tmp.append(perm[:i] + word[0:1] + perm[i:])
        return tmp


if __name__ == "__main__":
    print(dictionary())
