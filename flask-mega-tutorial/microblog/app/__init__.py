#!virtual/bin/python

from flask import Flask

app = Flask(__name__) # Imports target this Flask instance.
from app import views


# Shebang line doesnt work for some reason, just use path/to/virtual/python prog.py