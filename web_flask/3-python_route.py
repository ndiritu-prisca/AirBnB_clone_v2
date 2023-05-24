#!/usr/bin/python3
"""
    A script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """A function that returns hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """A function that diplays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """A function that diplays C followed by value of text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route("/python/")
@app.route("/python/<text>")
def python(text="is cool"):
    """A function that diplays Python followed by value of text"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
