#!/usr/bin/env python

"""
Flask server returning the result of an arbitrary function.
"""

from flask import Flask
from darwinday import days_to_dday

# make a Flask app
app = Flask(__name__)

# serve the result of this function to /
@app.route("/")
def days():
    """
    returns the days to Darwin Day string to the server address
    """
    return f"{days_to_dday()} days until Darwin Day"


if __name__ == '__main__':
    app.run(debug=True)
