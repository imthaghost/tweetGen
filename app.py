import os
import sys
from src.vose import *
from flask import Flask, render_template, redirect, url_for, request, jsonify
import json

app = Flask(__name__)
words = get_words('thus.txt')
histogram = sample2dist(words)
vose = VoseAlias(histogram)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
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
        yeet = vose.sample_n(size=num)
        # "I don't want to do this logic shit, ben just do it for me" - Gary
        sentence = ' '.join(yeet).capitalize() + '.'
        return jsonify({'sentence': sentence})


if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run(debug=True, port=8080)
