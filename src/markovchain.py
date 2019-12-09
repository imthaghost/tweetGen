
""" Markov Chain generator

In mathematical terms, a Markov Chain is a sequence of values 
where the next value depends only on the current value (and not past values). 
It's basically a really simple state machine, where 
given the present state, the future state is conditionally independent of the past.
Markov chains have many real-world applications. For example, Google's Page Rank 
algorithm is essentially a Markov chain over a graph of the web.
One of the simplest and most well known applications of Markov Chains 
is generating "realistic" looking texts based on some set of input texts.
In the case of text, a Markov Chain could be used to answer the question, 
"Given the present word (or set of words), which words might possibly follow?". 
You could also use Markov Chains to answer the question, 
"Given the present word, how likely is it that this word I've chosen would be the next?".
"""

# Built-in Python Modules
import re
import random
from collections import defaultdict, deque
# Local Python Modules


class MarkovChain:

    def __init__(self, num_key_words=2):
        """
        :param: num_key_words 
            :type: int - default 2
            :description: is the number of words that compose a key (suggested: 2 or 3)
        """
        self.num_key_words = num_key_words
        self.lookup_dict = defaultdict(list)
        self._punctuation_regex = re.compile('[/,.!;\?\:\-\[\]\(\)\"\\\n]+')
        self._seeded = False
        self.__seed_me()

    def __seed_me(self, rand_seed=None):
        if self._seeded is not True:
            try:
                if rand_seed is not None:
                    random.seed(rand_seed)
                else:
                    random.seed()
                self._seeded = True
            except NotImplementedError:
                self._seeded = False

    """
  " Build Markov Chain from data source.
  " Use add_file() or add_string() to add the appropriate format source
  """

    def add_file(self, file_path):
        content = ''
        with open(file_path, 'r') as fh:
            self.__add_source_data(fh.read())

    def add_string(self, str):
        self.__add_source_data(str)

    def __add_source_data(self, str):
        clean_str = self._punctuation_regex.sub(' ', str).lower()
        tuples = self.__generate_tuple_keys(clean_str.split())
        for t in tuples:
            self.lookup_dict[t[0]].append(t[1])

    def __generate_tuple_keys(self, data):
        if len(data) < self.num_key_words:
            return

        for i in range(len(data) - self.num_key_words):
            yield [tuple(data[i:i+self.num_key_words]), data[i+self.num_key_words]]

    def generate_text(self, max_length=50):
        """Generates text based on the data the Markov Chain contains"""
        # max_length is the maximum number of words to generate
        context = deque()
        output = []
        if len(self.lookup_dict) > 0:
            self.__seed_me(rand_seed=len(self.lookup_dict))

            idx = random.randint(0, len(self.lookup_dict)-1)
            chain_head = list(self.lookup_dict.keys())[idx]
            context.extend(chain_head)

            while len(output) < (max_length - self.num_key_words):
                next_choices = self.lookup_dict[tuple(context)]
                if len(next_choices) > 0:
                    next_word = random.choice(next_choices)
                    context.append(next_word)
                    output.append(context.popleft())
                else:
                    break
            output.extend(list(context))
        return output


if __name__ == "__main__":
    mc = MarkovChain()
    mc.add_file('/Users/ghost/Projects/tweetGen/corpus/thus.txt')
    print(mc.generate_text())
