__author__ = 'dhruv'

import pickle

with open("classifier.pickle", "rb") as f:
    classifier = pickle.load(f)

classifier.show_most_informative_features()