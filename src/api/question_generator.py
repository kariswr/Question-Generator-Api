from flask_restful import Resource, reqparse

from src.preprocess.prepare_free_input import prepare_featured_input

import os

class InferenceQuestion(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('paragraph', required=True)
        parser.add_argument('answer', required=True, type=list, action='append')
        
        args = parser.parse_args()
       
        answer_in_order = prepare_featured_input(args.paragraph, output_file_name='test.txt', manual_ne_postag=False, lower=True, seed=42, answers=args.answer)
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
        
        print('Finish generating questions....')

        i = 0
        qas = []
        while (i < len(questions) and i < len(answer_in_order)):
            qas.append({'question': questions[i], 'answer': answer_in_order[i]})
            i += 1

        print(qas)

        return {"qas" : qas}, 200