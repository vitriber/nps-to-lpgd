import sys
from repository.database import DataBase

class Enterprise:
    def get_all():
        try:
            query = 'select * from "Enterprise"'
            return DataBase.select(query)           
        except Exception as ex:            
            error = "Enterprise Repository - get_all error: {}".format(ex)
            raise Exception(error)          

    def get_by_id(id): 
        try:             
            query = 'select * from "Enterprise" where Id = {}'.format(id)
            return DataBase.select(query)
        except Exception as ex:            
            error = "Enterprise Repository - get_by_id error: {}".format(ex)
            raise Exception(error)

    def add(
        name,
        question_1, 
        question_2,
        question_3,
        question_4,
        question_5,
        question_7,
        question_8,
        question_9,
        question_10,
        question_11,
        question_12,
        question_13,
        question_14,
        question_15,
        nps
    ):
        try:
            query = """INSERT INTO public."Enterprise"(name, question_1, question_2, question_3, question_4, question_5, question_7, question_8, question_9, question_10, question_11, question_12, question_13, question_14, question_15, nps)
                       VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\'\'{}\', \'{}\', \'{}\', \'{}\'); """.format(
                            name,
                            question_1, 
                            question_2,
                            question_3,
                            question_4,
                            question_5,
                            question_7,
                            question_8,
                            question_9,
                            question_10,
                            question_11,
                            question_12,
                            question_13,
                            question_14,
                            question_15,
                            nps
                        )
            return DataBase.insert(query)
        except Exception as ex:            
            error = "Enterprise Repository - add error: {}".format(ex)
            raise Exception(error)
    
    def update(
        id,
        name,
        question_1, 
        question_2,
        question_3,
        question_4,
        question_5,
        question_7,
        question_8,
        question_9,
        question_10,
        question_11,
        question_12,
        question_13,
        question_14,
        question_15,
        nps
    ):
        try:
            query = """UPDATE INTO public."Enterprise"
                       SET(name, question_1, question_2, question_3, question_4, question_5, question_7, question_8, question_9, question_10, question_11, question_12, question_13, question_14, question_15, nps)
                       VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\'\'{}\', \'{}\', \'{}\', \'{}\')
                       WHERE id = {}; """.format(
                            name,
                            question_1, 
                            question_2,
                            question_3,
                            question_4,
                            question_5,
                            question_7,
                            question_8,
                            question_9,
                            question_10,
                            question_11,
                            question_12,
                            question_13,
                            question_14,
                            question_15,
                            nps,
                            id
                        )
            return DataBase.update(query)
        except Exception as ex:            
            error = "Enterprise Repository - add error: {}".format(ex)
            raise Exception(error)