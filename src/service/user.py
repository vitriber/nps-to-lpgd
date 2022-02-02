from repository.user import User as RepositoryUser
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from util import Util
import json

class User:
    def get_all():
        try:
            data = RepositoryUser.get_all()    
            if(data):
                return data
        except Exception as ex:
            error = "User Service - get_all error: {}".format(ex)
            raise Exception(error)            

    def get_by_id(id):    
        try:            
            data = RepositoryUser.get_by_id(id)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:            
            error = "User Service - get_by_id error: {}".format(ex)
            raise Exception(error)

    def insert_user(user):
        try:
            name = user.get('name')
            mail = user.get('mail')
            phone = user.get('phone')
            password = user.get('password')
            password = generate_password_hash(password, method='sha256')
            is_admin = user.get('is_admin')

            user_to_add = RepositoryUser.add(
                name, 
                mail,
                phone,
                password,
                is_admin
            )
            return user_to_add
        except Exception as ex:            
            error = "User Service - insert_user error: {}".format(ex)
            raise Exception(error)
    
    def update_user(id, user):
        try:
            name = user.get('name')
            mail = user.get('mail')
            phone = user.get('phone')
            password = user.get('password')
            password = generate_password_hash(password, method='sha256')
            is_admin = user.get('is_admin')

            user_to_update = RepositoryUser.update(
                id,
                name, 
                mail,
                phone,
                password,
                is_admin
            )
            return user_to_update
        except Exception as ex:            
            error = "User Service - update_user error: {}".format(ex)
            raise Exception(error)

    def login(user):
        try:
            email = user.get("email")
            password = user.get("password")
            user_response = RepositoryUser.login(email)

            if not user_response or not check_password_hash(user_response[0]['password'], password):
                return {"message": "Email ou senha incorretos"}, 401

            access_token = create_access_token(identity=email)
            response = {
                "access_token": access_token,
                "id": user_response[0]['id'],
                "email": user_response[0]['mail'],
                "is_admin": user_response[0]['is_admin'],
                "name": user_response[0]['name'],
            }
            return response
        except Exception as ex:            
            error = "User Service - login error: {}".format(ex)
            raise Exception(error)

    def signup(user):
        try:
            name = user.get('name')
            mail = user.get('mail')
            phone = user.get('phone')
            password = user.get('password')
            password = generate_password_hash(password, method='sha256')
            is_admin = False

            user_response = RepositoryUser.login(mail)

            if user_response:
                return {"msg": "Email já existe"}, 401

            user_to_add = RepositoryUser.add(
                name, 
                mail,
                phone,
                password,
                is_admin
            )

            access_token = create_access_token(identity=mail)
            response = {
                "access_token": access_token,
                "id": user_to_add[0][0],
                "email": user_to_add[0][2],
                "is_admin": user_to_add[0][5],
            }
            return response
        except Exception as ex:            
            error = "User Service - login error: {}".format(ex)
            raise Exception(error)