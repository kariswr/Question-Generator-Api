from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse
from os.path import dirname
import ast
import sys
import pandas as pd
from fuzzywuzzy import fuzz

sys.path.insert(1, dirname(dirname(sys.path[0])))

from question_generator import InferenceQuestion
from answer_grader import GradeAnswer

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

api.add_resource(InferenceQuestion, '/get-question')
api.add_resource(GradeAnswer, '/get-score')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)