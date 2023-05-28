from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
app = Flask(__name__)
api = Api(app)


# load
with open('model.pkl', 'rb') as f:
    clf2 = pickle.load(f)

clf2.predict([[4]])

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')


class predict(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']
        # make a prediction
        output = clf2.predict(user_query)
        return output

try:
    api.add_resource(predict, '/')
except:
    print("Error")

import requests
url = 'http://127.0.0.1:5000/'
params ={'query': [[3]]}
response = requests.get(url, params)
response.json()