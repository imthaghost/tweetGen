from dictionary_words import time_it  # import time decorator
import re  # regular expression library


class histogram(dict):
    """
    A histogram object of type dict

    """

    def __init__(self, path=None):
        super(histogram, self).__init__()
        self.path = path

    def get_value(self):
        """
        """

    def sample(self, frequency):
        """

        """


# def histogram(path):
#     """returns a histogram data structure that stores each unique word along with
#     the number of times that the word appears in the source text

#         Parameters
#         ----------
#         path : str,
#             path to file that contains text you want to create a histogram for

#         Returns
#         ----------
#         historgram: dict,
#             key value pair - (the unique words and amount of times the word appears)

#         Raises
#         ------
#         TypeError
#             If no parameters were given...requires 1 positional argument
#         """
#     some_words = []
#     # open the text file
#     with open(path, 'r') as f:
#         # convert all words to lowecase to catch exceptions and edge cases
#         words = f.read().lower()
#         # create a words list
#         words_list = re.sub(r'[^a-zA-Z\s]', '', words)
#         # reassign the list
#         some_words = words_list.split()
#     # create histogram
#     histogram = {}
#     # find all words
#     for word in some_words:
#         if word:
#             histogram[word] = histogram.get(word, 0) + 1
#     return histogram


# def frequency(word, histogram):
#     """returns a histogram data structure that stores each unique word along with
#     the number of times that the word appears in the source text

#         Parameters
#         ----------
#         path : str,
#             path to file that contains text you want to create a histogram for

#         Returns
#         ----------
#         historgram: dict,
#             key value pair - (the unique words and amount of times the word appears)

#         Raises
#         ------
#         TypeError
#             If no parameters were given...requires 1 positional argument
#         """
#     word = word.lower()
#     if isinstance(histogram, dict):
#         return histogram.get(word, 0)
#     # if isinstance(histogram, list):
#     #     return [x for x in histogram print(x)]
