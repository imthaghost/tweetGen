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
    with open(path, "r") as file:
        words = file.read().split('\n')
        word_list = []
        for i in range(int(num)):
            word_list.append(
                choice(words))
        return ' '.join(word_list).capitalize() + '.'


def get_word(path='/usr/share/dict/words'):
    with open(path, "r") as file:
        word = file.read().split('\n')
        rand_word = choice(word)
        return rand_word


if __name__ == "__main__":
    print(dictionary())
