import os
import random
from flask import Flask, render_template, Markup, flash, jsonify, request

# Variables
app = Flask(__name__)
app.config['SECRET_KEY'] = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
words = ''

# Load words
with open('words.txt', 'r') as file:
    words = file.read().splitlines()

# Functions
def generate_word():
    random.shuffle(words)
    word_one = words[random.randint(0, len(words)-1)]
    word_two = words[random.randint(0, len(words)-1)]
    print('Word Generated: {}{}'.format(word_one, word_two))
    return '{}{}'.format(word_one, word_two)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_lag_ord')
def lag_ord():
    return jsonify(result=(generate_word()))

# Start
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')