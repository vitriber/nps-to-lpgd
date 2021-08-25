from Repository.enterprise import Enterprise
from util import Util

class Enterprise:
    def get_all():
        try:
            data = RepositoryEnterprise.get_all()    
            if(data):
                return data
        except Exception as ex:
            error = "Enterprise Service - get_all error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def get_by_id(id):    
        try:            
            data = RepositoryEnterprise.get_by_id(id)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:            
            error = "Enteprise Service - get_by_id error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)