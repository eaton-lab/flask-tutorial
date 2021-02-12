#!/usr/bin/env python

"""
Load a CSV file into a relational database and set up an API to 
search by species name, locality ID, or accession ID and return
result in JSON format.
"""

import json
import pandas as pd
from flask import Flask
from flask_restful import Api, Resource, reqparse

# Define the app components
app = Flask(__name__)
api = Api(app)

# load the CSV database from publich URL
URL = "https://raw.githubusercontent.com/eaton-lab/eaton-lab.github.io/master/data/fieldnotes-2-11-2021.csv"
df = pd.read_csv(URL)

# parse arguments from the REST API at URL/?genus=Pedicularis&epithet=rex
parser = reqparse.RequestParser()
parser.add_argument("genus", type=str, help="genus (e.g., Pedicularis)")
parser.add_argument("epithet", type=str, help="specific epithet (e.g., rex)")
parser.add_argument("locality", type=int, help="locality ID (e.g., 100)")
parser.add_argument("accession", type=str, help="accession ID (e.g., DE200)")


class FieldNotes(Resource):
    def get(self):
        """
        parses API arguments to filter the dataframe and return as json
        """
        # get arguments from uri
        args = parser.parse_args()

        # make a copy of the database
        subdf = df.copy()

        # subset using selections
        if args.get('genus'):
            subdf = subdf[subdf.genus == args['genus']]
        if args.get('epithet'):
            subdf = subdf[subdf.species_epithet == args['epithet']]
        if args.get('locality'):
            subdf = subdf[subdf.locality == args['locality']]
        if args.get('accession'):
            subdf = subdf[subdf.accession == args['accession']]
        return json.loads(subdf.to_json())


# expose FieldNotes at index/
api.add_resource(FieldNotes, '/api')

if __name__ == '__main__':
    app.run(debug=True)
