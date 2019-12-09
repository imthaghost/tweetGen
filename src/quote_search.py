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
    context = quotes()
    who = 'plato'
    num = 900
    context._gen(who, num)
    print(context.quote)
