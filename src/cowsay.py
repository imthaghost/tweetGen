from sys import argv

art = """

        ( {}
           )  )
       ______(____
      (___________)
       /         \\
      /           \\
    |             |
 ____\             /____
()____'.__     __.'____()
      .'` .'```'. `-.
    ().'`       `'.()

"""


def cowsay(sentence):
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
    word = ' '.join(sentence)

    return art.format(word)


if __name__ == "__main__":
    print(cowsay(argv[1:]))

    # print(cowsay(sentence))
