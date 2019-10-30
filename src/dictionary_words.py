import os
from sys import argv
import time  # import time library
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
        rand_word_or_words_are_we_really_here_for_naming_convention = []
        for i in range(int(num)):
            rand_word_or_words_are_we_really_here_for_naming_convention.append(
                choice(words))
        return ' '.join(rand_word_or_words_are_we_really_here_for_naming_convention).capitalize() + '.'


def get_word(path='/usr/share/dict/words'):
    with open(path, "r") as yeet:
        word = yeet.read().split('\n')
        rand_word = choice(word)
        return rand_word


if __name__ == "__main__":
    print(dictionary())
