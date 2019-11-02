import numpy as np
import pandas as pd
from os import path
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from src.vose import get_words

# grab the words from file
# will convert this to web crawler later
words = get_words('thus.txt')
histogram = {}
get = histogram.get
for o in words:  # o for outcome
    histogram[o] = get(o, 0) + 1


# start converting container
outline = np.array(Image.open("./static/img/bird.png"))


def transform_format(val):
    if val == 0:
        return 255
    else:
        return val


transformed = np.ndarray((outline.shape[0], outline.shape[1]), np.int32)

for i in range(len(outline)):
    transformed[i] = list(map(transform_format, outline[i]))


wordcloud = WordCloud(max_font_size=50, max_words=100,
                      background_color="white", contour_width=1, mask=transformed)
wordcloud.generate_from_frequencies(frequencies=histogram)
src = wordcloud.to_file("./static/img/cloud.png")
