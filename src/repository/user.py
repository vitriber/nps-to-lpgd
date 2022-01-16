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
            query = 'select * from "user" where Id = {}'.format(id)
            return DataBase.select(query)
        except Exception as ex:            
            error = "User Repository - get_by_id error: {}".format(ex)
            raise Exception(error)

    def add(
        name,
        mail,
        phone,
        password
    ):
        try:
            query = """INSERT INTO public."user"(name, mail, phone, password)
                       VALUES (\'{}\', \'{}\', {}, \'{}\'); """.format(
                            name,
                            mail,
                            phone,
                            password
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
        password
    ):
        try:
            query = """UPDATE public."user"
                       SET
                           name = \'{}\', 
                           mail = \'{}\', 
                           phone = {}, 
                           password = \'{}\'
                       WHERE id = {}; """.format(
                            name,
                            mail, 
                            phone,
                            password,
                            id
                        )
            return DataBase.update(query)
        except Exception as ex:            
            error = "User Repository - update error: {}".format(ex)
            raise Exception(error)