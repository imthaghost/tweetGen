import os
from sys import argv



def dictionary(path):
    wordlist = open(path, 'r')
    words = []
    for word in wordlist:
        print(word.split('\n'))


if __name__ == "__main__":
    path = '/usr/share/dict/words'
    dictionary(path)
