import sys
from repository.database import DataBase

class QuestionaryUser:
    def add(
        user_id,
        questionary_id
    ):
        try:
            query = """INSERT INTO public."questionary_user"(user_id, questionary_id)
                       VALUES ({}, {}); """.format(
                            user_id,
                            questionary_id
                        )
            return DataBase.insert(query)
        except Exception as ex:            
            error = "Questionary Repository - add error: {}".format(ex)
            raise Exception(error)
    
    def delete(
        questionary_id
    ):
        try:
            query = 'DELETE FROM  "questionary_user" where questionary_id = {}'.format(questionary_id);
            return DataBase.update(query)
        except Exception as ex:            
            error = "Questionary Repository - delete error: {}".format(ex)
            raise Exception(error)