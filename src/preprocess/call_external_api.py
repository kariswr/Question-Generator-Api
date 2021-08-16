import http.client
import json


API_BASE_URL = 'api.prosa.ai'
API_KEY = ''
POS_TAG_PORT = '5500'
NER_PORT = '10009'

import ast
import json
import requests

def get_ner(text):
    url = "https://api.prosa.ai/v1/entities"
    payload = json.dumps({"text": text})
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    res = requests.post(url, data = payload, headers = headers)

    print(type(ast.literal_eval(res.text)))
    print(ast.literal_eval(res.text))
    return ast.literal_eval(res.text)

def get_pos_tag(text):
    url = "https://api.prosa.ai/v1/syntax"
    payload = json.dumps({
        "text": text, 
        "granularity": "coarse"})
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    res = requests.post(url, data = payload, headers = headers)

    res = ast.literal_eval(res.text)

    pos_tags = []
    for sentence in res['sentences']:
        temp_sentence = []
        for token in sentence['tokens']:
            temp_pos_tag = [token['token'], token['pos_tag']]
            temp_sentence.append(temp_pos_tag)
        pos_tags.append(temp_sentence)

    data = {'postags' : pos_tags}

    print(type(data))
    print(data)
    return data