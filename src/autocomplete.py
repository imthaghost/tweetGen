import sys


def complete(start, path="/usr/share/dict/words"):
    with open(path, 'r') as f:
        words = f.read().split()
    autocomplete_list = list()
    for word in words:
        if word.startswith(start):
            autocomplete_list.append(word)
    return autocomplete_list


if __name__ == '__main__':
    print(complete('hello'))
