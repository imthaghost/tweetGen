"""chain.py
wrapper implentation of generating sentences"""

# External Python Modules
import markovify

# Local Python Modules
import markovchain


def real_gen(corpus='/Users/ghost/Projects/tweetGen/corpus/plato_republic.txt'):
    mc = MarkovChain()
    mc.add_file(corpus)
    chain = ' '
    chain.join(mc.generate_text())


def gen_sentence(num=2, corpus='/Users/ghost/Projects/tweetGen/corpus/plato_republic.txt'):
    # Get raw text as string.
    with open(corpus) as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)
    sentence = []
    for i in range(num):
        sentence.append(text_model.make_sentence())

    return sentence


if __name__ == "__main__":
    text = gen_sentence(num=2)
    body = ' '
    body = body.join(text)
