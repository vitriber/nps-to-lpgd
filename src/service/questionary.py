from repository.questionary import Questionary as RepositoryQuestionary
from util import Util
import json

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

    def insert_questionary(user):
        try:
            name = user.get('name')

            questionary_to_add = RepositoryQuestionary.add(
                name
            )
            return questionary_to_add
        except Exception as ex:            
            error = "Questionary Service - insert_questionary error: {}".format(ex)
            raise Exception(error)
    
    def update_questionary(id, user):
        try:
            name = user.get('name')

            questionary_to_update = RepositoryQuestionary.update(
                id,
                name, 
            )
            return questionary_to_update
        except Exception as ex:            
            error = "Questionary Service - update_questionary error: {}".format(ex)
            raise Exception(error)
