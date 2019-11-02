import sys
import json
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from src.vose import *
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from flask import Flask, render_template, redirect, url_for, request, jsonify


app = Flask(__name__)
words = get_words('thus.txt')
histogram = sample2dist(words)
vose = VoseAlias(histogram)

# master histogram
master = {}
for o in words:  # o for outcome
    master[o] = master.get(o, 0) + 1


def transform_format(val):
    if val == 0:
        return 255
    else:
        return val

        # start creating outline


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    global master
    outline = np.array(Image.open("./static/img/bird.png"))
    transformed = np.ndarray(
        (outline.shape[0], outline.shape[1]), np.int32)
    for i in range(len(outline)):
        transformed[i] = list(map(transform_format, outline[i]))

    wordcloud = WordCloud(max_font_size=50, max_words=100,
                          background_color="white", mask=transformed)
    wordcloud.generate_from_frequencies(frequencies=master)

    wordcloud.to_file("./static/img/cloud.png")

    img = Image.open('./static/img/cloud.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("./static/img/better.png", "PNG")
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    num = request.form.get('count')
    if num == None or num == 0:
        yeet = vose.sample_n(size=10)
        sentence = ' '.join(yeet).capitalize() + '.'
        print('sentence:' + sentence)
        return jsonify({'sentence': sentence})
    else:
        sample = vose.sample_n(size=num)
        sentence = ' '.join(sample).capitalize() + '.'
        # rebuild  histogram
        return jsonify({'sentence': sentence})


if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run(debug=True, port=8080)
