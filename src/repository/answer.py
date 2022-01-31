import sys
from repository.database import DataBase

class Answer:
    def get_all():
        try:
            query = 'select * from "answer"';
            return DataBase.select(query)           
        except Exception as ex:            
            error = "Answer Repository - get_all error: {}".format(ex)
            raise Exception(error) 

    def get_all_by_questionary_id(id_questionary):
        try:
            query = 'select * from "answer" where questionary_id = {}'.format(id_questionary);
            return DataBase.select(query)           
        except Exception as ex:            
            error = "Answer Repository - get_all error: {}".format(ex)
            raise Exception(error)          

    def get_by_id(id_questionary, id): 
        try:             
            query = 'select * from "answer" where Id = {} and questionary_id = {}'.format(id, id_questionary)
            return DataBase.select(query)
        except Exception as ex:            
            error = "Answer Repository - get_by_id error: {}".format(ex)
            raise Exception(error)

    def add(
        id_questionary,
        id_question,
        value,
        date_now
    ):
        try:
            query = """INSERT INTO public."answer"(questionary_id, question_id, value, updated_at, created_at)
                       VALUES ({},{},{},\'{}\',\'{}\'); """.format(
                            id_questionary,
                            id_question,
                            value,
                            date_now,
                            date_now
                        )
            return DataBase.insert(query)
        except Exception as ex:            
            error = "Answer Repository - add error: {}".format(ex)
            raise Exception(error)