#!/usr/bin/env python3
"""A script creates a basic Babel app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


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
    """Renders a html template"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Determines the best match with our supported languages"""
    locale = request.args.get('locale')
    supported_langs = app.config['LANGUAGES']
    if locale and locale in supported_langs:
        return locale

    return request.accept_languages.best_match(supported_langs)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[None, Dict]:
    """Returns a user dictionary or None if the ID cannot be found or if login
    was not passed
    """
    user_id = request.args.get('login_as')
    try:
        user_id = int(user_id)
    except Exception:
        pass
    else:
        if user_id and user_id in users:
            return users[int(user_id)]


@babel.timezoneselector
def get_timezone():
    """Returns the timezone from which a request is made."""
    timezone = request.args.get('timezone')


@app.before_request
def before_request() -> None:
    """Finds a user if any and sets it as a global on flask.g.user"""
    g.user = get_user()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
