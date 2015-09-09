__author__ = 'dhruv'

from sklearn.datasets import load_svmlight_file

def load_data(path):
    X, y = load_svmlight_file(path)

    return X, y
