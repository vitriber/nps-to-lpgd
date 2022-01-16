import sys
from repository.database import DataBase

class Questionary:
    def get_all():
        try:
            query = 'select * from "questionary"'
            return DataBase.select(query)           
        except Exception as ex:            
            error = "Questionary Repository - get_all error: {}".format(ex)
            raise Exception(error)          

    def get_by_id(id): 
        try:             
            query = 'select * from "questionary" where Id = {}'.format(id)
            return DataBase.select(query)
        except Exception as ex:            
            error = "Questionary Repository - get_by_id error: {}".format(ex)
            raise Exception(error)

    def add(
        name,
    ):
        try:
            query = """INSERT INTO public."questionary"(name)
                       VALUES (\'{}\'); """.format(
                            name,
                        )
            return DataBase.insert(query)
        except Exception as ex:            
            error = "Questionary Repository - add error: {}".format(ex)
            raise Exception(error)
    
    def update(
        id,
        name,
    ):
        try:
            query = """UPDATE public."questionary"
                       SET
                           name = \'{}\', 
                       WHERE id = {}; """.format(
                            name,
                            id
                        )
            return DataBase.update(query)
        except Exception as ex:            
            error = "Questionary Repository - update error: {}".format(ex)
            raise Exception(error)