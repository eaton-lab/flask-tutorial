#!/usr/bin/env python

"""
Flask server returning the result of an arbitrary function at / 
and the results of a function that takes arguments based the URL 
string at /name/year/month/day, which is also wrapped in HTML+CSS
to look nice.
"""

from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
from darwinday import age_to_darwin

# Define the app
app = Flask(__name__)
api = Api(app)

# parse arguments for the REST API
parser = reqparse.RequestParser()
parser.add_argument("name", type=str, help="Name of person")
parser.add_argument("year", type=int, help="Birth year of person")
parser.add_argument("month", type=int, help="Birth month of person")
parser.add_argument("day", type=int, help="Birth date of person")


class DarwinDay(Resource):
    """
    get function calls GET to 
    """
    def __init__(self):
        self.args = parser.parse_args()

    def get(self):
        """
        returns JSON result of age_to_darwin func using parsed args
        """
        # get number of days
        ndays = age_to_darwin(
            self.args['year'], self.args['month'], self.args['day'])

        # get whether age is younger or older
        jdata = {
            'name': self.args['name'], 
            'ndays': ndays, 
            'direction': "younger" if ndays > 0 else "older",
        }
        return jdata



@app.route("/")
def index():
    """
    Render the JSON REST data as HTML on the index page, unless 
    arguments are missing, then simply show JSON error message.
    """
    # get api instance with parsed args
    inst = DarwinDay()

    # if parsed api args are not all present then print fail message
    missing_args = [i for (i, j) in inst.args.items() if j is None]
    if missing_args:
        return {
            "_message": f"missing REST API args: {missing_args}",
            "example-uri": "?name=joe&year=1955&month=3&day=5",
        }

    # else get the json data processed by api funcs
    jdata = inst.get()

    # convert json response to HTML and return it
    html = render_template(
        "template-1.html", 
        name=jdata['name'],
        days=jdata['ndays'],
        direction=jdata['direction'],
    )
    return html

# expose json data at /api/
api.add_resource(DarwinDay, '/api')     

if __name__ == '__main__':
    app.run(debug=True)
