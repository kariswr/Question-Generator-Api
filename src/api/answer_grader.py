from flask_restful import Resource, reqparse, inputs
from fuzzywuzzy import fuzz

import os
import re

punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
punctuations_regex = re.compile(r"([%s])" % punctuations)
def tokenize(s):
    s = re.sub(punctuations_regex, r"", s)
    s = s.split()
    print(s)
    return s

def count_score(s1, s2):
    min_len = min(len(s1), len(s2))
    total_word = len(s1) + len(s2)
    overlap = []
    i = 0
    while i < min_len:
        if (s1[0] in s2):
            overlap.append(s1[0])
            s2.remove(s1[0])
        s1.remove(s1[0])
        i += 1
    score = (2 * len(overlap)) / total_word * 100
    return score

class GradeAnswer(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('input', required=True)
        parser.add_argument('ground_truth', required=True)
        parser.add_argument('case_sensitive', type=inputs.boolean, default=False)
        parser.add_argument('threshold', required=True, type=int)
        parser.add_argument('character_based', type=inputs.boolean, default=False)
        
        args = parser.parse_args()

        str1 = args.input
        str2 = args.ground_truth
        if (not args.case_sensitive):
            str1 = str1.lower()
            str2 = str2.lower()

        if (not args.character_based):
            word_str1 = tokenize(str1)
            word_str2 = tokenize(str2)
            score = int(count_score(word_str1, word_str2))
        else : 
            score = fuzz.ratio(str1, str2)

        print(score)

        if (score >= args.threshold):
            result = 'correct'
        else :
            result = 'wrong'

        return {"score" : score, "result" : result}, 200