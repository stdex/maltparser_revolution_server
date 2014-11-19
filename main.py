#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request, url_for, render_template, abort
from werkzeug.debug import get_current_traceback

from scipy.sparse import *
from scipy import *
from sklearn.cross_validation import train_test_split#
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

#model_1
def initialize_sklearn_model():
    ka = joblib.load("models/model_02/ka.pkl")
    encoder = joblib.load("models/model_02/encoder.pkl")
    model_ka_RF = joblib.load("models/model_02/RandomForestClassifier.pkl")
    return ka, encoder, model_ka_RF

def parse_input(X_data, ka, encoder, model_ka_RF):
    # перекодируем значения в недсятичный вектор с помощью OneHotEncoder
    X_encode = encoder.transform(X_data)
    # преобразуем с использованием Nystroem
    X_data_transform = ka.transform(X_encode)
    val = model_ka_RF.predict(X_data_transform)
    return val


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/send_data/<req>', methods=['GET', 'POST'])
def send_data(req):
    if req == 'learn' and request.method == 'POST':
        try:
            # получение данных
            inp_data = request.stream.read().decode("utf-8")
            csv_r = csv.reader([inp_data], delimiter="\t")
            malt_data = []
            # на всякий случай цикл, вдруг во входном файле >одной строки.
            for row in csv_r:
                malt_data.append([float(x)+1 for x in row])

            ka, encoder, model_ka_RF = initialize_sklearn_model()
            # обрабатываем входные значения моделями sklearn
            val = parse_input(malt_data, ka, encoder, model_ka_RF)
            return '%s' % val

        except (Exception) as error:
            track = get_current_traceback(skip=1, show_hidden_frames=True, ignore_system_exceptions=False)
            track.log()
            abort(500)
    else:
        return ""

if __name__ == "__main__":
    app.run()




