import requests
from dictionary_words import time_it, get_word
import os
import json
from random import choice


@time_it
def game(key, wordlist='/usr/share/dict/words'):
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

    print('hmmmm let me think of a definition')
    # set the base uri
    base = 'https://dictionaryapi.com/api/v3/references/collegiate/json/{}?key=%s' % (
        api_key)
    # grab a random word
    word = get_word(path=wordlist)
    # set up the request url
    request_url = base.format(word)
    # create the request and dump the response
    response = requests.get(request_url).json()
    # check to see if the response is only words or a dictionary
    while not found(response):
        # generate a new word and send a request
        word = get_word(path=wordlist)
        # continue the game
        request_url = base.format(word)
        # create the request and dump the response
        response = requests.get(request_url).json()
    print('\n')
    definition = response[0]['shortdef']
    print(definition[0])
    print('can you guess the word that matches the definition?')
    print('\n')
    print(word)
    return word


def found(response):
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
    if isinstance(response[0], str):
        thinking = ['nope', 'not that one', 'oo thats too hard for you',
                    'hmmmm', 'thinking...', 'maybeee...']
        print(choice(thinking))
        return False
    else:
        print('found one for you!')
        return True


if __name__ == "__main__":
    # grab the api key
    api_key = os.environ.get('api_key')
    # play the game
    while True:
        print('ASSSUHHHH dude! Welcome to the vocab game')
        print('\n')
        some_word = game(api_key)
        word_guess = input('>> ')
        if some_word == word_guess:
            won = 'You guessed the correct word: {}'
            print('\x1b[1;32m' + won.format(some_word) + '\x1b[0m')
            break
