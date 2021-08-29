import flask
from flask import request, jsonify
from service.enterprise import Enterprise
import json

class Api:
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

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
    def api_enterprise_all():
        return jsonify(Enterprise.get_all())

    @app.route('/api/enterprise/<id>', methods=['GET'])
    def api_enterprise(id):    
        return jsonify(Enterprise.get_by_id(id))

    @app.route('/api/enterprise', methods=['POST'])
    def api_enterprise_insert():
        data = request.json
        Enterprise.insert_enterprise(data)
        return('Empresa adicionada com sucesso!')
    
    @app.route('/api/enterprise/<id>', methods=['PATCH'])
    def api_enterprise_update(id):
        data = request.json
        Enterprise.update_enterprise(id, data)
        return('Empresa atualizada com sucesso')
    
    @app.route('/api/enterprise/find-nps', methods=['POST'])
    def api_find_nps():
        data = request.json
        predictedNPS = Enterprise.find_nps(data)
        data_json = {"nps":predictedNPS}
        print('Esse é o valor do NPS:', data_json)
        return data_json

    app.run()