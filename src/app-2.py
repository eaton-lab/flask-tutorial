#!/usr/bin/env python

"""
Flask server returning the result of an arbitrary function at / 
and the results of a function that takes arguments based the URL 
string at /name/year/month/day, which is also wrapped in HTML+CSS
to look nice.
"""

from flask import Flask, render_template
from darwinday import days_to_dday, age_to_darwin

# Define the app
app = Flask(__name__)


@app.route("/")
def days():
    """
    returns a days until DDAY result
    """
    return f"{days_to_dday()} days until Darwin Day"


@app.route("/<string:name>/<int:year>/<int:month>/<int:day>")
def darwin_age(name, year, month, day):
    """
    returns a rendered HTML page with age difference result.
    """
    # get number of days
    ndays = age_to_darwin(year, month, day)

    # get whether age is younger or older
    direction = "younger" if ndays > 0 else "older"

    # stick result into HTML template
    return render_template(
        "template-1.html", name=name, days=ndays, direction=direction)


if __name__ == '__main__':
    app.run(debug=True)
