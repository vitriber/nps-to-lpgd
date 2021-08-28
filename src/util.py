import flask
import decimal
from flask import request
from unidecode import unidecode
from datetime import datetime
import pandas
from sklearn import linear_model

class Util:
    def get_nps(data, new):
        try:
            df = pandas.read_json(data)
            X = df[
                [
                    'Question1', 
                    'Question2',
                    'Question3',
                    'Question4',
                    'Question5',
                    'Question6',
                    'Question7',
                    'Question8',
                    'Question9',
                    'Question10',
                    'Question11',
                    'Question12',
                    'Question13',
                    'Question14',
                    'Question15',
                ]]
            y = df['NPS']

            regr = linear_model.LinearRegression()
            regr.fit(X, y)

            predictedNPS = regr.predict([[new.get('question_1'),
                new.get('question_1'),
                new.get('question_2'),
                new.get('question_3'),
                new.get('question_4'),
                new.get('question_5'),
                new.get('question_6'),
                new.get('question_7'),
                new.get('question_8'),
                new.get('question_9'),
                new.get('question_10'),
                new.get('question_11'),
                new.get('question_12'),
                new.get('question_13'),
                new.get('question_14')]])
        except:
            predictedNPS = ""
        return predictedNPS