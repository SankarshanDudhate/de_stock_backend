"""
    config.py
    - settings for the flask application object
"""


class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = 'my secret key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False