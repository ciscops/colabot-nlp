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
import yaml
import pandas as pd
from random import shuffle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
import pickle
import string


def get_commands():
    with open('colabot_commands.yaml', 'r') as f:
        commands = yaml.safe_load(f)
    list_of_tuples = list()
    for k in commands:
        for c in commands[k]:
            c = preprocess(c)
            list_of_tuples.append((k, c))
    return list_of_tuples


def generate_df(tuple_commands):
    shuffle(tuple_commands)
    df = pd.DataFrame(tuple_commands, columns=['y', 'x'])
    return df


def create_pipeline():
    return Pipeline([
        ('bow', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('classifier', SGDClassifier(loss='modified_huber', alpha=0.01))
    ])


def preprocess(text):
    text = [word.lower().strip().rstrip('s') for word in text.split()]
    text = [''.join(c for c in s if c not in string.punctuation) for s in text]
    return [' '.join(x for x in text if x)][0]


if __name__ == '__main__':
    cmds = get_commands()
    df = generate_df(cmds)
    final_pipeline = create_pipeline()
    final_pipeline.fit(df['x'], df['y'])
    with open('model.pickle', 'wb') as f:
        pickle.dump(final_pipeline, f, protocol=pickle.HIGHEST_PROTOCOL)
