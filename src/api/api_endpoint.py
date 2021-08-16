from flask import Flask
from flask_restful import Resource, Api, reqparse
from os.path import dirname
import ast
import sys
import pandas as pd

sys.path.insert(1, dirname(dirname(sys.path[0])))

from question_generator import InferenceQuestion


app = Flask(__name__)
api = Api(app)

api.add_resource(InferenceQuestion, '/get-question')

if __name__ == '__main__':
    app.run()