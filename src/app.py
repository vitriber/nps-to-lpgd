import os
import flask
import json

from flask import request, jsonify
from datetime import datetime, timedelta, timezone
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager, create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies

from service.enterprise import Enterprise
from service.user import User
from service.questionary import Questionary
from service.question import Question
from service.answer import Answer
from service.nps import NPS


class Api:
    app = flask.Flask(__name__)
    cors = CORS(app, resources={r"/foo": {"origins": "*"}})

    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config.from_object(os.environ.get('APP_SETTINGS'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "please-remember-to-change-me"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    jwt = JWTManager(app)

    @app.after_request
    def refresh_expiring_jwts(response):
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity())
            return response
        except (RuntimeError, KeyError):
            # Case where there is not a valid JWT. Just return the original respone
            return response


    @app.route('/api/login', methods=["POST"])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def login():
        data = request.json
        response = User.login(data)
        return response

    @app.route("/api/logout", methods=["POST"])
    def logout():
        response = jsonify({"msg": "logout successful"})
        unset_jwt_cookies(response)
        return response

    @app.route('/api/signup', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def signup():
        data = request.json
        response = User.signup(data)
        return(response)

    @app.errorhandler(404)
    def page_not_found(e):
        return "<h1>404</h1><p>The resource could not be found.</p>", 404

    @app.route('/', methods=['GET'])
    def home():
        return '''<h1>Api to calculate NPS according to answer enterprise</h1>
    <p>A prototype of API to calculate NPS according to answer entreprise</p>'''

    """ 
        User Controller
    """
    @app.route('/api/user/all', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_user_all():
        return jsonify(User.get_all())

    @app.route('/api/user/<id>', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_user(id):
        return jsonify(User.get_by_id(id))

    @app.route('/api/user', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_user_insert():
        data = request.json
        User.insert_user(data)
        return(json.dumps('User create with success!'))

    @app.route('/api/user/<id>', methods=['PATCH'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_user_update(id):
        data = request.json
        User.update_user(id, data)
        return(json.dumps('User updated with success'))

    """ 
        Enterprise Controller
    """

    @app.route('/api/user/enterprise/all', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_enterprise_all():
        return jsonify(Enterprise.get_all())

    @app.route('/api/user/<user_id>/enterprise/', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_enterprise(user_id):
        return jsonify(Enterprise.get_by_id(user_id))

    @app.route('/api/user/<user_id>/enterprise/', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_enterprise_insert(user_id):
        data = request.json
        Enterprise.insert_enterprise(user_id, data)
        return(json.dumps('Enterprise created with success!'))

    @app.route('/api/user/<user_id>/enterprise/<id>', methods=['PATCH'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_enterprise_update(user_id, id):
        data = request.json
        Enterprise.update_enterprise(user_id, id, data)
        return(json.dumps('Enterprise updated with success'))

    """ 
        Questionary Controller
    """
    @app.route('/api/questionary/all', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_questionary_all():
        return jsonify(Questionary.get_all())

    @app.route('/api/questionary/<id>', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_questionary(id):
        return jsonify(Questionary.get_by_id(id))

    @app.route('/api/questionary', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_questionary_insert():
        data = request.json
        return(jsonify(Questionary.insert_questionary(data)))

    @app.route('/api/questionary/<id>', methods=['PATCH'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_questionary_update(id):
        data = request.json
        Questionary.update_questionary(id, data)
        return(json.dumps('Questionary created with success'))

    """ 
        Question Controller
    """
    @app.route('/api/question/all', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_question_all():
        return jsonify(Question.get_all())
    

    @app.route('/api/question/<id>', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_question(id):
        return jsonify(Question.get_by_id(id))

    @app.route('/api/question', methods=["POST"])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_question_insert():
        data = request.json
        Question.insert_question(data)
        return(json.dumps('Question created with success!'))

    @app.route('/api/question/<id>', methods=['PATCH'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_question_update(id):
        data = request.json
        Question.update_question(id, data)
        return(json.dumps('Question updated with success'))

    """ 
        Answer Controller
    """
    @app.route('/api/answer/all/', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_answer_all():
        return jsonify(Answer.get_all())

    @app.route('/api/answer/all/<id_questionary>', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_answer_all_by_questionary_id(id_questionary):
        return jsonify(Answer.get_all_by_questionary_id(id_questionary))

    @app.route('/api/answer/<id_questionary>/<id>', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_answer(id_questionary, id):
        return jsonify(Answer.get_by_id(id_questionary, id))

    @app.route('/api/answer/<id_questionary>', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_answer_insert(id_questionary):
        data = request.json
        Answer.insert_answer(id_questionary, data)
        return(json.dumps('Answer created with success!'))

    """ 
        NPS Controller
    """

    @app.route('/api/find-nps/', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def api_find_nps():
        data = request.json
        predictedNPS = NPS.find_nps(data)
        data_json = {"nps": predictedNPS}
        return data_json

    if __name__ == '__main__':
        app.run()
