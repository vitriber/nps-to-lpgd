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
            query = 'select * from "questionary" where id = {}'.format(id)
            return DataBase.select(query)
        except Exception as ex:            
            error = "Questionary Repository - get_by_id error: {}".format(ex)
            raise Exception(error)
    
    def get_by_name_enterprise(name_enterprise): 
        try:             
            query = 'SELECT * FROM "questionary" where "name_enterprise" = {}'.format(name_enterprise)
            return DataBase.select(query)
        except Exception as ex:            
            error = "Questionary Repository - get_by_id error: {}".format(ex)
            raise Exception(error)

    def add(
        name_enterprise,
        date_now
    ):
        try:
            query = """INSERT INTO public."questionary"(name_enterprise, updated_at, created_at)
                       VALUES (\'{}\', \'{}\', \'{}\'); """.format(
                            name_enterprise,
                            date_now,
                            date_now
                        )
            return DataBase.insert(query)
        except Exception as ex:            
            error = "Questionary Repository - add error: {}".format(ex)
            raise Exception(error)
    
    def update(
        id,
        name_enterprise,
        date_now
    ):
        try:
            query = """UPDATE public."questionary"
                       SET
                           name_enterprise = \'{}\',
                           updated_at = \'{}\'  
                       WHERE id = {}; """.format(
                            name_enterprise,
                            date_now,
                            id
                        )
            return DataBase.update(query)
        except Exception as ex:            
            error = "Questionary Repository - update error: {}".format(ex)
            raise Exception(error)