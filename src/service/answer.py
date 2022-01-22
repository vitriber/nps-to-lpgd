from repository.answer import Answer as RepositoryAnswer
from datetime import datetime
from util import Util
import json

class Answer:
    def get_all_by_questionary_id(id_questionary):
        try:
            data = RepositoryAnswer.get_all_by_questionary_id(id_questionary)    
            if(data):
                return data
        except Exception as ex:
            error = "Answer Service - get_all error: {}".format(ex)
            raise Exception(error)            

    def get_by_id(id_questionary, id):    
        try:            
            data = RepositoryAnswer.get_by_id(id_questionary, id)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:            
            error = "Answer Service - get_by_id error: {}".format(ex)
            raise Exception(error)

    def insert_answer(id_questionary, id_question, answer):
        try:
            value = answer.get('value')
            date_now = datetime.now()

            question_to_add = RepositoryAnswer.add(
                id_questionary,
                id_question,
                value, 
                date_now
            )
            return question_to_add
        except Exception as ex:            
            error = "Answer Service - insert_answer error: {}".format(ex)
            raise Exception(error)