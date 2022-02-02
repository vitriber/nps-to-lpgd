import json

from flask import jsonify

from repository.questionary import Questionary as RepositoryQuestionary
from repository.questionary_user import QuestionaryUser as RepositoryQuestionaryUser
from datetime import datetime

class Questionary:
    def get_all():
        try:
            data = RepositoryQuestionary.get_all()    
            if(data):
                return data
        except Exception as ex:
            error = "Questionary Service - get_all error: {}".format(ex)
            raise Exception(error)            

    def get_by_id(id):    
        try:            
            data = RepositoryQuestionary.get_by_id(id)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:            
            error = "Questionary Service - get_by_id error: {}".format(ex)
            raise Exception(error)

    def insert_questionary(enterprise):
        try:
            name_enterprise = enterprise.get('name_enterprise')
            user_id = enterprise.get('user_id')
            nps_value = enterprise.get('nps_value')
            date_now = datetime.now() 

            questionary_to_add = RepositoryQuestionary.add(
                name_enterprise,
                nps_value,
                date_now
            )

            RepositoryQuestionaryUser.add(user_id, questionary_to_add[0][0])

            return questionary_to_add
        except Exception as ex:            
            error = "Questionary Service - insert_questionary error: {}".format(ex)
            raise Exception(error)
    
    def update_questionary(id, enterprise):
        try:
            name_enterprise = enterprise.get('name_enterprise')
            nps_value = enterprise.get('nps_value')
            date_now = datetime.now() 

            questionary_to_update = RepositoryQuestionary.update(
                id,
                name_enterprise,
                nps_value,
                date_now 
            )
            return questionary_to_update
        except Exception as ex:            
            error = "Questionary Service - update_questionary error: {}".format(ex)
            raise Exception(error)
