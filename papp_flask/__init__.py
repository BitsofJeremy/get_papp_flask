# Import the Flask basics
from flask import Flask, flash, redirect, url_for
from flask_bootstrap import Bootstrap
import logging


# Define the App
app = Flask(__name__)
app.config.from_pyfile('../config.py')

Bootstrap(app)

#
# Module Imports
#

# Import the module / component using their blueprints
from papp_flask.home.views import home

# Register Blueprints
app.register_blueprint(home)

