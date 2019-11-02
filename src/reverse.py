def reverse(Sentence):
    """Returns a given word in reverse 

        Parameters
        ----------
        Sentence : str,
            Any given string

        Raises
        ------
        TypeError
            If no parameters passed
        """
    # Spliting the Sentence into list of words.
    words = Sentence.split(" ")
    # List Comprehension Technique
    something = list()
    something = [x for]
    newWords = [word[::-1] for word in words]

    # Joining the new list of words to for a new Sentence
    newSentence = " ".join(newWords)

    return newSentence


def bad_reverse(string):
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
    return string[::-1]
