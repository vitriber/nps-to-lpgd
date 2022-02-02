import sys
from repository.database import DataBase

class Questionary:
    def get_all():
        try:
            query = 'select * from "questionary" ORDER BY id'
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
        nps_value,
        date_now
    ):
        try:
            query = """INSERT INTO public."questionary"(name_enterprise, nps_value, updated_at, created_at)
                       VALUES (\'{}\', {}, \'{}\', \'{}\'); """.format(
                            name_enterprise,
                            nps_value,
                            date_now,
                            date_now
                        )
            query_return = "SELECT * FROM questionary ORDER BY id DESC limit 1"
            return DataBase.insert(query, query_return)
        except Exception as ex:            
            error = "Questionary Repository - add error: {}".format(ex)
            raise Exception(error)
    
    def update(
        id,
        name_enterprise,
        nps_value,
        date_now
    ):
        try:
            query = """UPDATE public."questionary"
                       SET
                           name_enterprise = \'{}\',
                           nps_value = \'{}\',
                           updated_at = \'{}\' 
                       WHERE id = {}; """.format(
                            name_enterprise,
                            nps_value,
                            date_now,
                            id
                        )
            return DataBase.update(query)
        except Exception as ex:            
            error = "Questionary Repository - update error: {}".format(ex)
            raise Exception(error)