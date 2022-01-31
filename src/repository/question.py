import sys
from repository.database import DataBase

class Question:
    def get_all():
        try:
            query = 'SELECT * FROM "question" ORDER BY id'
            return DataBase.select(query)           
        except Exception as ex:            
            error = "Question Repository - get_all error: {}".format(ex)
            raise Exception(error)          

    def get_by_id(id): 
        try:             
            query = 'SELECT * FROM "question" WHERE id = {}'.format(id)
            return DataBase.select(query)
        except Exception as ex:            
            error = "Questionary Repository - get_by_id error: {}".format(ex)
            raise Exception(error)

    def add(
        name,
        description,
        constant_factor,
        date_now,
        is_multiple
    ):
        try:
            query = """INSERT INTO public."question"(name,description, constant_factor, updated_at, created_at, is_multiple)
                       VALUES (\'{}\', \'{}\',{}, \'{}\', \'{}\', {}); """.format(
                            name,
                            description,
                            constant_factor,
                            date_now,
                            date_now,
                            is_multiple
                        )
            return DataBase.insert(query)
        except Exception as ex:            
            error = "Question Repository - add error: {}".format(ex)
            raise Exception(error)
    
    def update(
        id,
        name,
        description,
        constant_factor,
        date_now,
        is_multiple
    ):
        try:
            query = """UPDATE public."question"
                       SET
                           name = \'{}\',
                           description = \'{}\',
                           constant_factor = {},
                           updated_at = \'{}\',
                           is_multiple = {}  
                       WHERE id = {}; """.format(
                            name,
                            description,
                            constant_factor,
                            date_now,
                            is_multiple,
                            id
                        )
            return DataBase.update(query)
        except Exception as ex:            
            error = "Question Repository - update error: {}".format(ex)
            raise Exception(error)