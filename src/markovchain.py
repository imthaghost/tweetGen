
""" Markov Chain generator

In mathematical terms, a Markov Chain is a sequence of values 
where the next value depends only on the current value (and not past values). 
It's basically a really simple state machine, where 
given the present state, the future state is conditionally independent of the past.
Markov chains have many real-world applications. For example, Google's Page Rank 
algorithm is essentially a Markov chain over a graph of the web.

"""

# Built-in Python Modules
import re
import random
from collections import defaultdict, deque  # only used for stretch challenge
# Local Python Modules
#from . import linkedlist
#from . import de_que
#from dictogram import Dictogram


class MarkovChain:
    """n-th order Markov Chain"""

    def __init__(self, order=2):
        """
        :param: order 
            :type: int - default 2
            :description: the number of words that compose a key (tested with 2-5 im sure strange) at some point i feel like if you go beyond a certain number the sentance returned will just be exactly the same with one or two words changed depending on what you set max_length to lmao 
        """
        self.order = order  # key for each state
        self.lookup_dict = defaultdict(list)
        self._punctuation_regex = re.compile(
            '[/,.!;\?\:\-\[\]\(\)\"\\\n]+')  # exclusion
        self._seeded = False  # default seed value
        self._gen_seed()  # generate see values

    def _gen_seed(self, rand_seed=None):
        """_gen_seed"""
        if self._seeded is not True:
            try:
                if rand_seed is not None:
                    random.seed(rand_seed)
                else:
                    random.seed()
                self._seeded = True
            except NotImplementedError:
                self._seeded = False

    def add_file(self, file_path):
        """Build Markov Chain from file data source"""
        content = ''
        with open(file_path, 'r') as fh:
            self.__add_source_data(fh.read())

    def add_string(self, str):
        """Build Markov Chain from string data source"""
        self.__add_source_data(str)

    def __add_source_data(self, str):
        """Cleanup functionality"""
        clean_str = self._punctuation_regex.sub(' ', str).lower()
        tuples = self.__generate_tuple_keys(clean_str.split())
        for t in tuples:
            self.lookup_dict[t[0]].append(t[1])

    def __generate_tuple_keys(self, data):
        """Our keys are tuples for space efficiency"""
        if len(data) < self.order:
            return

        for i in range(len(data) - self.order):
            yield [tuple(data[i:i+self.order]), data[i+self.order]]

    def generate_text(self, max_length=20):
        """Generates text based on the data the Markov Chain contains deafult 10"""
        # max_length is the maximum number of words to generate
        # todo implement deque from linked list class
        context = deque()
        # store the retured text
        output = []
        # check
        if len(self.lookup_dict) > 0:
            self._gen_seed(rand_seed=len(self.lookup_dict))

            idx = random.randint(0, len(self.lookup_dict)-1)
            chain_head = list(self.lookup_dict.keys())[idx]
            context.extend(chain_head)

            while len(output) < (max_length - self.order):
                next_choices = self.lookup_dict[tuple(context)]
                if len(next_choices) > 0:
                    next_word = random.choice(next_choices)
                    context.append(next_word)
                    output.append(context.popleft())
                else:
                    break
            output.extend(list(context))
        return output


# class Chain(Dictogram):
#     super().__init__()  # intialize Chain as a new Dictogram object where each key is a list


if __name__ == "__main__":
    # test
    mc = MarkovChain()
    mc.add_file('/Users/ghost/Projects/tweetGen/corpus/plato_republic.txt')
    print(mc.generate_text())
