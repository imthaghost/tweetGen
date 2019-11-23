"""
Flask Web Application
"""


import sys
import json
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from src.vose import *
from src.dictogram import *
from threading import Thread
import matplotlib.pyplot as plt
from multiprocessing import Process, Manager, Pool
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from flask import Flask, render_template, redirect, url_for, request, jsonify

# name of application
app = Flask(__name__)
# generate corpus I will convert this to webcrawler later
histogram = Dictogram(path='./corpus/thus.txt')
# construct alias tables
vose = VoseAlias(histogram)


def generation(file):
    histogram = {}
    # genration function for master historgram
    if os.stat(file).st_size == 0:
        raise IOError(
            "Please provide a file containing a corpus (not an empty file).")
    # Ensure the file is text based (not binary). This is based on the implementation
    #  of the Linux file command
    textchars = bytearray([7, 8, 9, 10, 12, 13, 27]) + \
        bytearray(range(0x20, 0x100))
    with open(file, "rb") as bin_file:
        if bool(bin_file.read(2048).translate(None, textchars)):
            raise IOError("Please provide a file containing text-based data.")
    with open(file, "r") as corpus:
        words = corpus.read().lower()
        words_list = re.sub(r'[^a-zA-Z\s]', '', words).split()

    for o in words_list:  # o for outcome
        histogram[o] = histogram.get(o, 0) + 1
    return histogram


def transform_format(val):
    # helper function for transforming image colors
    if val == 0:
        return 255
    else:
        return val


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    """ root/index route
    @GET:
        summary: index endpoint will render file 'index.html'
        description: Get
        responses:
            200:
                description: index.html returned
                schema: indexSchema
            404:
                description: index not found.
    """
    # master histogram
    # generate a courpus
    # use the master histogram not the alias table
    master = generation('./corpus/thus.txt')
    # this will be the outline of our wordlcoud image
    outline = np.array(Image.open("./static/img/bird.png"))
    # convert image rgb bytes to an array
    transformed = np.ndarray(
        (outline.shape[0], outline.shape[1]), np.int32)
    # transform image from inside out
    for i in range(len(outline)):
        transformed[i] = list(map(transform_format, outline[i]))
    # setup word cloud with a mask of our trasnformed image
    wordcloud = WordCloud(max_font_size=50, max_words=100,
                          background_color="white", mask=transformed)
    # generate the word cloud from histogram - master
    wordcloud.generate_from_frequencies(frequencies=master)
    # export word cloud to file
    wordcloud.to_file("./static/img/cloud.png")
    # open the newly generated image
    img = Image.open('./static/img/cloud.png')
    # convert the image to have an alpha property
    img = img.convert("RGBA")
    # grab the data of the image
    datas = img.getdata()
    # new data array
    newData = []
    # convert all white space to be white with an alpha of 0
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    # put data into an array
    img.putdata(newData)
    # save our new image as png
    img.save("./static/img/better.png", "PNG")
    # render the index page
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """ generate

    @POST:
        summary:
        description:
        responses:
            200:
                description:
                    POST request recieved by server
            500:
                description:
                    server encounted exception
    """
    num = request.form.get('count')
    if num == None or num == 0:
        sample = vose.sample_n(size=10)
        sentence = ' '.join(sample).capitalize() + '.'
        print('sentence:' + sentence)
        return jsonify({'sentence': sentence})
    else:
        sample = vose.sample_n(size=num)
        sentence = ' '.join(sample).capitalize() + '.'
        return jsonify({'sentence': sentence})


class generation(object):
    __init__(self, file):
        self.file = file


if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'  # set enviornment variable
    app.run(debug=True, port=8080)  # start the flask application
