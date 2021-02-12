#!/usr/bin/env python

"""
Flask server returning the result of an arbitrary function at / 
and the result of a function that takes arguments based the URL 
string at /name/year/month/day.
"""

from flask import Flask
from darwinday import days_to_dday, age_to_darwin

# Define the app
app = Flask(__name__)

# Define the functions and routes they are served at
@app.route("/")
def days():
    """
    returns a days until dday result
    """
    return f"{days_to_dday()} days until Darwin Day"


@app.route("/<string:name>/<int:year>/<int:month>/<int:day>")
def darwin_age(name, year, month, day):
    """
    returns a age to darwin result
    """
    # get number of days
    ndays = age_to_darwin(year, month, day)
    direction = "younger" if ndays > 0 else "older"
    return f"{name} is {ndays} days {direction} than Darwin"


if __name__ == '__main__':
    app.run(debug=True)
