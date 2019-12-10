"""qoute_search.py
literally just a wrapper for a nice tool that finds quotes
"""
# Built-in Python Modules
# none :)
# External Python Modules
from quote import quote


def get_some_quotes(query, ammount):
    text = quote(query, ammount)
    return text


if __name__ == "__main__":

    who = 'zeus'
    num = 2
    context = get_some_quotes(who, num)
    if not context:
        # todo: raise NoneFound error from errors.py
        print('No text was found on this name')
    else:
        print(context)
