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
    word = ' '.join(sentence)

    return art.format(word)


if __name__ == "__main__":
    print(cowsay(argv[1:]))

    # print(cowsay(sentence))
