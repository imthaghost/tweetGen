from random import shuffle, choice, randint
from sys import argv


def lit_rearrange(words):
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
    # create a copy of words just for Alan
    words_list = list(words)
    # shuffle words
    shuffle(words_list)
    # return joined words list
    return ' '.join(words_list)


def rearrange(words):
    """
     Description: since I can't use shuffle because of Alan im just
     going to implement Fisher-Yates Shuffle algorithm

        params:
            words: list, a list of words the user wishes to shuffle
    """
    # using Fisher–Yates shuffle Algorithm
    for i in range(len(words)):

        # Pick a random index from 0 to i
        j = randint(0, i)

        # Swap arr[i] with the element at random index
        words[i], words[j] = words[j], words[i]
    return str(words)


if __name__ == "__main__":

    args = argv[1:]
    words = rearrange(args)
    print(words)
