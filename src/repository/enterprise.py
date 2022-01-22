import sys
from repository.database import DataBase

class Enterprise:
    def get_all():
        try:
            query = 'select * from "enterprise"'
            return DataBase.select(query)           
        except Exception as ex:            
            error = "Enterprise Repository - get_all error: {}".format(ex)
            raise Exception(error)          

    def get_by_id(id): 
        try:             
            query = 'select * from "enterprise" where user_id = {}'.format(id)
            return DataBase.select(query)
        except Exception as ex:            
            error = "Enterprise Repository - get_by_id error: {}".format(ex)
            raise Exception(error)

    def add(
        user_id,
        name,
        mail,
        phone,
    ):
        try:
            query = """INSERT INTO public."enterprise"(user_id, name, mail, phone)
                       VALUES ({}, \'{}\', \'{}\', \'{}\'); """.format(
                            user_id,
                            name,
                            mail,
                            phone
                        )
            return DataBase.insert(query)
        except Exception as ex:            
            error = "Enterprise Repository - add error: {}".format(ex)
            raise Exception(error)
    
    def update(
        user_id,
        id,
        name,
        mail,
        phone
    ):
        try:
            query = """UPDATE public."enterprise"
                       SET
                           user_id = {}
                           name = \'{}\', 
                           mail = \'{}\', 
                           phone = {}, 
                       WHERE id = {}; """.format(
                            user_id,
                            name,
                            mail, 
                            phone,
                            id
                        )
            return DataBase.update(query)
        except Exception as ex:            
            error = "Enterprise Repository - add error: {}".format(ex)
            raise Exception(error)