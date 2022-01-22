from repository.enterprise import Enterprise as RepositoryEnterprise
from util import Util
import json

class Enterprise:
    def get_all():
        try:
            data = RepositoryEnterprise.get_all()    
            if(data):
                return data
        except Exception as ex:
            error = "Enterprise Service - get_all error: {}".format(ex)
            raise Exception(error)            

    def get_by_id(user_id):    
        try:            
            data = RepositoryEnterprise.get_by_id(user_id)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:            
            error = "Enteprise Service - get_by_id error: {}".format(ex)
            raise Exception(error)

    def insert_enterprise(user_id, enterprise):
        try:
            name = enterprise.get('name')
            mail = enterprise.get('mail')
            phone = enterprise.get('phone')

            enterprise_to_add = RepositoryEnterprise.add(
                user_id,
                name, 
                mail,
                phone,
            )
            return enterprise_to_add
        except Exception as ex:            
            error = "Enterprise Service - insert_enterprise error: {}".format(ex)
            raise Exception(error)
    
    def update_enterprise(user_id, id, user):
        try:
            name = user.get('name')
            mail = user.get('mail')
            phone = user.get('phone')

            enterprise_to_update = RepositoryEnterprise.update(
                user_id,
                id,
                name, 
                mail,
                phone,
            )
            return enterprise_to_update
        except Exception as ex:            
            error = "Enterprise Service - update_enterprise error: {}".format(ex)
            raise Exception(error)

