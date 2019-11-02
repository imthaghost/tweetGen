import os
import sys
import time
from bs4 import BeautifulSoup as bs
import requests


def time_it(func):
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
