from flask_restful import Resource, reqparse

from src.preprocess.prepare_free_input import prepare_featured_input

import os

class InferenceQuestion(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('paragraph', required=True)
        parser.add_argument('answer', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary
       
        prepare_featured_input(args.paragraph, output_file_name='test.txt', manual_ne_postag=False, lower=True, seed=42)
        preprocessed_file_path = 'test.txt'

        print('Generating questions...')
        os.system(
            f'onmt_translate -model models/final/gru_037_step_32100.pt \
                -src test.txt \
                -output free_input_001_pred.txt -replace_unk \
                -beam_size 2 \
                -max_length 22'
        )

        questions = []
        with open('free_input_001_pred.txt', 'r') as f_in:
            predictions = f_in.readlines()
        for prediction in predictions:
            questions.append(prediction.strip())
        
        print(questions)
        print('Finish generating questions....')

        return {"questions" : questions}, 200