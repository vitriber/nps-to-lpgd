from Repository.database import DataBase

class Entreprise:
    def get_all():        
        query = 'select * from "Enterprise"'
        return DataBase.select(query)            

    def get_by_id(id):                
        query = 'select * from "City" where Id = {}'.format(id)
        return DataBase.select(query)     