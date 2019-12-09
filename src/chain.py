"""chain.py
wrapper implentation of generating sentences using markovify"""

# External Python Modules
import markovify


if __name__ == "__main__":
    # Get raw text as string.
    with open('/Users/ghost/Projects/tweetGen/corpus/plato_republic.txt') as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)

    # Print five randomly-generated sentences
    for i in range(5):
        print(text_model.make_sentence())

    # Print three randomly-generated sentences of no more than 280 characters
    for i in range(3):
        print(text_model.make_short_sentence(280))
