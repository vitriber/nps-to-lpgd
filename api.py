import flask
from flask import request, jsonify
from Service.enterprise import Enterprise

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

    @app.route('/api/v1/enterprise/all', methods=['GET'])
    def api_enterprise_all():
        return jsonify(Enterprise.get_all())

    @app.route('/api/enterprise', methods=['GET'])
    def api_district():    
        id = 1
        return jsonify(Enterprise.get_by_id(id))

    app.run()