import flask
import decimal
from flask import request
from unidecode import unidecode
from datetime import datetime
import pandas
from sklearn import linear_model
import json

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
        
    def get_nps(data, answer):
        try:
            df = pandas.read_json(json.dumps(data)).fillna(0)
            keys = list(data[len(data) - 1].keys())
            keys.remove('nps_value')

            X = df[keys]
            y = df['nps_value']

            regr = linear_model.LinearRegression()
            regr.fit(X, y)

            format_answers = {}
            for key in answer:
                if key['question_id'] not in format_answers:
                    format_answers['question_' + str(key['question_id'])] = key['value']
            format_answers["constant_factor"] = 1
            predictedNPS = regr.predict([list(format_answers.values())])

        except:
            predictedNPS = ""
        return predictedNPS[0]