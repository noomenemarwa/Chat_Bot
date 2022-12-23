import nltk #Natural Language Toolkit
nltk.download('punkt') # give token for each words
from nltk.strem.lancaster import LancasterStemmer # return the origin words (doing ==> do)
stemmer= LancasterStemmer()

import numpy as np 
import tensorflow as tf # learning
import tflearn 
import random # randem  response
import json # use to read json file
import pickle

from time import sleep

# read intents file
with open("intents.json") as file:
    data = json.load(file)


# create four lists
words =[] # to save words after tokenized
labels= []  # to save tags
docs_x = []  # to save words without takensets
docs_y =[] # to save relation between words and tag

for intent in data["intents"]:
    for patterns in intent["patterns"]:
        word = nltk.word_tokenize(patterns)
        words.extend(word)
        docs_x.append(word)
        docs_y.append(intent["tag"])
    if intent['tag'] not in labels:
        labels.append(intent['tag'])

# 
words = [stemmer.stem(w.lower()) for w in words w != "?"]
# 
words = sorted(list(set(words)))
# 
labels= sorted(labels)
# 
training = []
output = []
# 
out_empty = [ 0 for _ in range(len(labels))]