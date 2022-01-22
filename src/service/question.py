from repository.question import Question as RepositoryQuestion
from datetime import datetime
from util import Util
import json

class Question:
    def get_all(id_questionary):
        try:
            data = RepositoryQuestion.get_all()    
            if(data):
                return data
        except Exception as ex:
            error = "Question Service - get_all error: {}".format(ex)
            raise Exception(error)            

    def get_by_id(id_questionary, id):    
        try:            
            data = RepositoryQuestion.get_by_id(id)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:            
            error = "Question Service - get_by_id error: {}".format(ex)
            raise Exception(error)

    def insert_question(id_questionary, question):
        try:
            name = question.get('name')
            constant_factor = question.get('constant_factor')
            date_now = datetime.now()

            question_to_add = RepositoryQuestion.add(
                id_questionary,
                name, 
                constant_factor,
                date_now
            )
            return question_to_add
        except Exception as ex:            
            error = "Question Service - insert_question error: {}".format(ex)
            raise Exception(error)
    
    def update_question(id_questionary, id, question):
        try:
            name = question.get('name')
            constant_factor = question.get('constant_factor')
            date_now = datetime.now()

            user_to_update = RepositoryQuestion.update(
                id_questionary,
                id,
                name, 
                constant_factor,
                date_now
            )
            return user_to_update
        except Exception as ex:            
            error = "Question Service - update_question error: {}".format(ex)
            raise Exception(error)
