from flask_restful import Resource, reqparse, inputs
from fuzzywuzzy import fuzz

import os

class GradeAnswer(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('input', required=True)
        parser.add_argument('ground_truth', required=True)
        parser.add_argument('case_sensitive', type=inputs.boolean, default=False)
        parser.add_argument('threshold', required=True, type=int)
        
        args = parser.parse_args()

        str1 = args.input
        str2 = args.ground_truth
        if (not args.case_sensitive):
            score = fuzz.ratio(str1.lower(), str2.lower())
        else :
            score = fuzz.ratio(str1, str2)
        print(score)

        if (score >= args.threshold):
            result = 'correct'
        else :
            result = 'wrong'

        return {"score" : score, "result" : result}, 200