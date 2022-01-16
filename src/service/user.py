from repository.user import User as RepositoryUser
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

            user_to_add = RepositoryUser.add(
                name, 
                mail,
                phone,
                password
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
            password = user.get('phone')

            user_to_update = RepositoryUser.update(
                id,
                name, 
                mail,
                phone,
                password
            )
            return user_to_update
        except Exception as ex:            
            error = "User Service - update_user error: {}".format(ex)
            raise Exception(error)
