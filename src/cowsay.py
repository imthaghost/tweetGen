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
    return art.format(sentence)


if __name__ == "__main__":
    args = argv
    for x in args:
        print(cowsay(x))
