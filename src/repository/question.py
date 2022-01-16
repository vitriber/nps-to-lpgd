import sys
from repository.database import DataBase

class Question:
    def get_all(id_questionary):
        try:
            query = 'select * from "question" where questionary_id = {}'.format(id_questionary);
            return DataBase.select(query)           
        except Exception as ex:            
            error = "Question Repository - get_all error: {}".format(ex)
            raise Exception(error)          

    def get_by_id(id_questionary, id): 
        try:             
            query = 'select * from "question" where Id = {} and questionary_id = {}'.format(id, id_questionary)
            return DataBase.select(query)
        except Exception as ex:            
            error = "Questionary Repository - get_by_id error: {}".format(ex)
            raise Exception(error)

    def add(
        id_questionary,
        name,
        constant_factor
    ):
        try:
            query = """INSERT INTO public."question"(questionary_id, name,  constant_factor)
                       VALUES ({},\'{}\', {}); """.format(
                            id_questionary,
                            name,
                            constant_factor
                        )
            return DataBase.insert(query)
        except Exception as ex:            
            error = "Question Repository - add error: {}".format(ex)
            raise Exception(error)
    
    def update(
        id_questionary,
        id,
        name,
        constant_factor
    ):
        try:
            query = """UPDATE public."question"
                       SET
                           name = \'{}\',
                           constant_factor = {} 
                       WHERE id = {} and questionary_id = {}; """.format(
                            name,
                            constant_factor,
                            id,
                            id_questionary
                        )
            return DataBase.update(query)
        except Exception as ex:            
            error = "Question Repository - update error: {}".format(ex)
            raise Exception(error)