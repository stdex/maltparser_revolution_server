from flask import Flask
from flask import request

from scipy.sparse import *
from scipy import *
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
import logging
import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.kernel_approximation import Nystroem
import datetime

app = Flask(__name__)

encoder = OneHotEncoder()
encoder = joblib.load("models/model_00/encoder.pkl")

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/send_data/<req>', methods=['GET', 'POST'])
def send_data(req):
    if req == 'learn' and request.method == 'POST':
        data = request.stream.read().decode("utf-8")
        return '%s' % data

if __name__ == "__main__":
    app.run()

