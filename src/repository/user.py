import sys
from repository.database import DataBase

class User:
    def get_all():
        try:
            query = 'select * from "user"'
            return DataBase.select(query)           
        except Exception as ex:            
            error = "User Repository - get_all error: {}".format(ex)
            raise Exception(error)          

    def get_by_id(id): 
        try:             
            query = 'select * from "user" where id = {}'.format(id)
            return DataBase.select(query)
        except Exception as ex:            
            error = "User Repository - get_by_id error: {}".format(ex)
            raise Exception(error)

    def add(
        name,
        mail,
        phone,
        password,
        is_admin
    ):
        try:
            query = """INSERT INTO public."user"(name, mail, phone, password, is_admin)
                       VALUES (\'{}\', \'{}\', \'{}\', \'{}\', {}); """.format(
                            name,
                            mail,
                            phone,
                            password,
                            is_admin
                        )
            return DataBase.insert(query)
        except Exception as ex:            
            error = "User Repository - add error: {}".format(ex)
            raise Exception(error)
    
    def update(
        id,
        name,
        mail,
        phone,
        password,
        is_admin
    ):
        try:
            query = """UPDATE public."user"
                       SET
                           name = \'{}\', 
                           mail = \'{}\', 
                           phone = \'{}\', 
                           password = \'{}\',
                           is_admin = {}
                       WHERE id = {}; """.format(
                            name,
                            mail, 
                            phone,
                            password,
                            is_admin,
                            id
                        )
            return DataBase.update(query)
        except Exception as ex:            
            error = "User Repository - update error: {}".format(ex)
            raise Exception(error)