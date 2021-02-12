#!/usr/bin/env python

"""
Testing the API to return JSON formatted data
"""

import requests

BASE = "http://127.0.0.1:5000/"

# gets the webpage results from app
# response  = requests.get(BASE + "api/deren/1985/3/30")
# print(response.text)


# app-3.py
response  = requests.get(
	BASE + "", 
	params={
		"name": "deren", 
		# "year": 1900,
		"month": 2,
		"day": 20,
	})

print(response.json())
# print(response.json())


# # gets the json result from api
# response  = requests.get(BASE + "args", params={"locality": 9})
# print(response.json())

# response  = requests.get(BASE, params={"genus": "Pedicularis", "epithet": "rex"})
# print(response.url)
# print(response.json())

