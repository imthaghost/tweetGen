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

## https://github.com/tempor1s/tweetgen/blob/master/lib/bin/anagram.py ###

## works if you use sets ####


def get_real_anagram(s):
    """
    Get all the anagrams for a given word
    Params:
        s: The word that you want to get all the anagrams for
    Returns:
        set: All of the anagrams
    """
    anagrams_variations = get_anagram(s)
    words = get_set_words_from_file('/usr/share/dict/words')

    return anagrams_variations.intersection(words)
    # real_words = []
    # for word in words:
    #     if word in anagrams_variations:
    #         real_words.append(word)

    # # for word in anagrams_variations:
    # #     if word in words:
    # #         real_words.append(word)

    # return real_words
## works if you use sets ####
