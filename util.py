import flask
import decimal
from flask import request
from unidecode import unidecode
from datetime import datetime

class Util:
    host = 'localhost'
    database = 'nps-to-lgpd'
    user = 'postgres'
    password = '12345'    