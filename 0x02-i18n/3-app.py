#!/usr/bin/env python3
"""A script creates a basic Babel app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Union


class Config(object):
    """Translate the application to French"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def get_index() -> str:
    """Renders the a html template"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Determines the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
