__author__ = 'dhruv'

import re, math, collections, itertools, os
import numpy as np
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import RegexpTokenizer


import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist

def generate_vocabulary():
    """ Read in the vocabulary for the imdb movie reviews
    :return: word2id - a dictionary of (word, id)
    """

    count = 0
    word2id = dict()
    with open("data/in/aclImdb/imdb.vocab", "r") as f:
        for line in f:
            word2id[line.strip("\n")] = count
            count += 1
    return word2id


def wordcount_vector(sentence: str, word2id: dict):
    vector = np.zeros((len(word2id)))
    tk = RegexpTokenizer(r'\w+(-\w+)*')
    st = LancasterStemmer()
    words = []
    for word in sentence.split(" "):
        words.extend(tk.tokenize(word))

    for word in words:
        word = st.stem((word))
        try:
            vector[word2id[word]] += 1
        except KeyError:
            print(word, "not in vocabulary")
    return vector


def wordcount_matrix(sentence):
    count = 0
    pos_sentences = []
    for filename in os.listdir("data/in/aclImdb/train/pos/"):
        if filename.endswith(".txt"):
            count += 1
            with open("data/in/aclImdb/train/pos/" + filename) as f:
                pos_sentences.append((f.read()))

            print(filename)

if __name__ == '__main__':

    test_vocab = {"dog": 0, "cat": 1}