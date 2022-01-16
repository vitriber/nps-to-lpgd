import flask
import decimal
from flask import request
from unidecode import unidecode
from datetime import datetime
import pandas
from sklearn import linear_model

class Util:
    def get_field(name, type):
        try:
            if (type == 'int'):
                field = int(request.args.get(name, 0))
            elif (type == 'float'):
                field = float(request.args.get(name, 0))
            elif (type == 'bool'):                
                field = request.args.get(name, '').lower() in ('true', 'True')                
            elif (type == 'str'):
                field = str(request.args.get(name, ''))
            else:
                return "Util Error: Type {} not implemented.".format(type)
        except:
            field = ""
        return field
        
    def get_nps(data, new):
        try:
            df = pandas.read_json(data)
            X = df[
                [
                    'question_1', 
                    'question_2',
                    'question_3',
                    'question_4',
                    'question_5',
                    'question_6',
                    'question_7',
                    'question_8',
                    'question_9',
                    'question_10',
                    'question_11',
                    'question_12',
                    'question_13',
                    'question_14',
                    'question_15',
                    'constant_factor'
                ]]
            y = df['nps']

            regr = linear_model.LinearRegression()
            regr.fit(X, y)

            question_1 = (new.get('question_1') and 1) or 0
            question_2 = (new.get('question_2') and 1) or 0
            question_3 = (new.get('question_3') and 1) or 0
            question_4 = (new.get('question_4') and 1) or 0
            question_5 = (new.get('question_5') and 1) or 0
            question_6 = (new.get('question_6') and 1) or 0
            question_7 = (new.get('question_7') and 1) or 0
            question_8 = (new.get('question_8') and 1) or 0
            question_9 = (new.get('question_9') and 1) or 0
            question_10 = (new.get('question_10') and 1) or 0
            question_11 = (new.get('question_11') and 1) or 0
            question_12 = (new.get('question_12') and 1) or 0
            question_13 = (new.get('question_13') and 1) or 0
            question_14 = (new.get('question_14') and 1) or 0
            question_15 = (new.get('question_15') and 1) or 0
            constant_factor = 1

            predictedNPS = regr.predict([[
                question_1, 
                question_2,
                question_3,
                question_4,
                question_5,
                question_6,
                question_7,
                question_8,
                question_9,
                question_10,
                question_11,
                question_12,
                question_13,
                question_14,
                question_15,
                constant_factor]])

        except:
            predictedNPS = ""
        return predictedNPS[0]