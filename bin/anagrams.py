from dictionary_words import time_it


@time_it
def anagram(word):
    """Returns random words from a file 

        Parameters
        ----------
        word : str
            Word in which we will return all permutations of

        Raises
        ------
        TypeError
            If no no or 1 parameter was given...requires two keyword parameters path and ammount
        """
    if len(word) <= 1:
        return word
    else:
        tmp = []
        for perm in anagram(word[1:]):
            for i in range(len(word)):
                tmp.append(perm[:i] + word[0:1] + perm[i:])
        return tmp

################################### Generator ############################


@time_it
def anagram_gen(word):
    if len(word) <= 1:
        yield word
    else:
        for perm in anagram(word[1:]):
            for i in range(len(word)):
                yield perm[:i] + word[0:1] + perm[i:]

################################### Generator ############################
