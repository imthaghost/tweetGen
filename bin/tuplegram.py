def tuple_histogram(file):
    """
   Tuple version of a histogram from a text file
    """
    with open file as f:
        histo = []
        for words in f:
        count = 0
        for word in words:
            if word == words:
                count += 1
        tup = (word, count)
        if tup not in histo:
            histo.append(tup)
    return histo
