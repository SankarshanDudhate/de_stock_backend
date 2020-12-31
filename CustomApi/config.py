"""
    config.py
    - settings for the flask application object
"""


class BaseConfig(object):
	DEBUG = True
	SECRET_KEY = 'my secret key'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:bootcamp@localhost/ilx'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	PRESERVE_CONTEXT_ON_EXCEPTION = False