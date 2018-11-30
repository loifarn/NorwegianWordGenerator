import os
import random
from flask import Flask, render_template, Markup, flash, jsonify, request

# Variables
app = Flask(__name__)
app.config['SECRET_KEY'] = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
words = ''
current_word = ''

# Load words
with open('words.txt', 'r') as file:
    words = file.read().splitlines()
# words = words.split(',')

# Functions
def generate_word():
    random.shuffle(words)
    word_one = words[random.randint(0, len(words)-1)]
    word_two = words[random.randint(0, len(words)-1)]
    print('Word Generated: {}{}'.format(word_one, word_two))
    current_word = '{}{}'.format(word_one, word_two)
    return '{}{}'.format(word_one, word_two)

# Routes
@app.route('/')
def index():
    flash(Markup('<h1>{word}</h1>'.format(word=generate_word())))
    return render_template('index.html')

@app.route('/_lag_ord')
def lag_ord():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = generate_word()
    return jsonify(result=c)

# Start
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port='80')
    app.run()