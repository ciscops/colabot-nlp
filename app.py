#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
from config import DefaultConfig as CONFIG
import logging
import string
from flask import Response
from flask import Flask
from flask import request
from flask import jsonify
import pickle


FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='zzzlogs.log', level=logging.INFO, format=FORMAT)
app = Flask(__name__)


def predict_thread(phrase, model):
    preprocessed = preprocess(phrase)
    result = model.predict([preprocessed])
    score = model.score([phrase], result)
    logging.info('command: ' + '"' + str(result[0]) + '"' + ' confidence: ' + str(float(score) * 100))
    return {'text': str(result[0]), 'confidence': str(float(score) * 100)}


def preprocess(text):
    text = [word.lower().strip().rstrip('s') for word in text.split()]
    text = [''.join(c for c in s if c not in string.punctuation) for s in text]
    return [' '.join(x for x in text if x)][0]


@app.route('/api/v1/nlp',  methods=['POST', 'GET'])
def server_route():
    results = ''
    if request.method == 'GET':
        status_code = Response(status=200)
        return status_code
    elif request.method == 'POST':
        logging.info(request.json)
        logging.info(request.method)
        logging.info(request)
        data = request.json
        try:
            if data.get('secret', '') == CONFIG.NLP_SECRET:
                logging.info('Secret Matched!')
                with open('model.pickle', 'rb') as g:
                    f_pipeline = pickle.load(g)
                results = predict_thread(data['text'], f_pipeline)
                logging.info('Made it past results')
                return jsonify(results)
            else:
                status_code = Response(status=403)
                return status_code
        except:
            logging.warning('Malformed body format in POST from {ip}. / Received body was {body}'
                            .format(ip=request.remote_addr, body=data))
            status_code = Response(status=403)
            return status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
