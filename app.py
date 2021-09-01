import os
import flask
import json

from flask import request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

from service.enterprise import Enterprise

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Api to calculate NPS according to answer enterprise</h1>
<p>A prototype API to calculate NPS according to anwer entreprise</p>'''

""" 
    Enterprise Controller
"""

@app.route('/api/enterprise/all', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_enterprise_all():
    return jsonify(Enterprise.get_all())

@app.route('/api/enterprise/<id>', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_enterprise(id):    
    return jsonify(Enterprise.get_by_id(id))

@app.route('/api/enterprise', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_enterprise_insert():
    data = request.json
    Enterprise.insert_enterprise(data)
    return(json.dumps('Empresa adicionada com sucesso!'))

@app.route('/api/enterprise/<id>', methods=['PATCH'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_enterprise_update(id):
    data = request.json
    Enterprise.update_enterprise(id, data)
    return(json.dumps('Empresa atualizada com sucesso'))

@app.route('/api/enterprise/find-nps', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_find_nps():
    data = request.json
    predictedNPS = Enterprise.find_nps(data)
    data_json = {"nps":predictedNPS}
    return data_json

if __name__ == '__main__':
    app.run()