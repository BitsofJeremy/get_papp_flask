# config.py

from logging.config import dictConfig
import os

"""
Common configurations
"""

# Put any configurations here that are common across all environments

# Name of the app
APP_NAME = 'app'
HOST = '127.0.0.1'
PORT = '5000'

DEBUG = True
FLASK_DEBUG = 1

# Threads
THREADS_PER_PAGE = 2

# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data. Default: MD5 of "secret"
CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY')

# Secret key for signing cookies
SECRET_KEY = os.getenv('SECRET_KEY')

# Salt for Tokens
SALTY_SECRET = os.getenv('SALTY_SECRET')

# Alchemy API Key from ENV
ALCHEMY_API_KEY = os.getenv('ALCHEMY_API_KEY')

# Define logging dict
dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '{"date": "%(asctime)s", '
                      '"log_level": "%(levelname)s", '
                      '"module": "%(module)s", '
                      '"message": "%(message)s"}'
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': 'app.log',
            'maxBytes': 1024000,
            'backupCount': 3
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': [
            'wsgi',
            'file'
        ]
    }
})


