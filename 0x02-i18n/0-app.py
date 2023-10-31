#!/usr/bin/env python3
"""A script to setup a basic Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world() -> str:
    """A basic Flask app"""
    return render_template('0-index.html', name=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
