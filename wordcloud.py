import numpy as np
import pandas as pd
from os import path
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import *
from src.vose import *


words = get_words('thus.txt')
histogram = sample2dist(words)
vose = VoseAlias(histogram)
print(vose)
histo = vose.sample_n(size=10)
df = pd.DataFrame.from_dict(histo)
print(df.head())
