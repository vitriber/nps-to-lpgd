from repository.enterprise import Enterprise as RepositoryEnterprise
from util import Util
import json

class Enterprise:
    def get_all():
        try:
            data = RepositoryEnterprise.get_all()    
            if(data):
                return data
        except Exception as ex:
            error = "Enterprise Service - get_all error: {}".format(ex)
            raise Exception(error)            

    def get_by_id(id):    
        try:            
            data = RepositoryEnterprise.get_by_id(id)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:            
            error = "Enteprise Service - get_by_id error: {}".format(ex)
            raise Exception(error)

    def find_nps(new):
        try:
            data = RepositoryEnterprise.get_all()
            data_json = json.dumps(data)
            predictedNPS = Util.get_nps(data_json, new)
            if(predictedNPS):
                return predictedNPS
            return 'Não foi possível realizar o calculo'
        except Exception as ex:            
            error = "Enteprise Service - find_nps error: {}".format(ex)
            raise Exception(error)

    def insert_enterprise(enterprise):
        try:
            name = enterprise.get('name')
            question_1 = enterprise.get('question_1')
            question_2 = enterprise.get('question_2')
            question_3 = enterprise.get('question_3')
            question_4 = enterprise.get('question_4')
            question_5 = enterprise.get('question_5')
            question_6 = enterprise.get('question_6')
            question_7 = enterprise.get('question_7')
            question_8 = enterprise.get('question_8')
            question_9 = enterprise.get('question_9')
            question_10 = enterprise.get('question_10')
            question_11 = enterprise.get('question_11')
            question_12 = enterprise.get('question_12')
            question_13 = enterprise.get('question_13')
            question_14 = enterprise.get('question_14')
            question_15 = enterprise.get('question_15')
            nps = enterprise.get('nps')
            constant_factor = True

            enterprise_to_add = RepositoryEnterprise.add(
                name, 
                question_1, 
                question_2,
                question_3,
                question_4,
                question_5,
                question_6,
                question_7,
                question_8,
                question_9,
                question_10,
                question_11,
                question_12,
                question_13,
                question_14,
                question_15,
                nps,
                constant_factor
            )
            return enterprise_to_add
        except Exception as ex:            
            error = "Enteprise Service - insert_enterprise error: {}".format(ex)
            raise Exception(error)
    
    def update_enterprise(id, enterprise):
        try:
            name = enterprise.get('name')
            question_1 = enterprise.get('question_1')
            question_2 = enterprise.get('question_2')
            question_3 = enterprise.get('question_3')
            question_4 = enterprise.get('question_4')
            question_5 = enterprise.get('question_5')
            question_6 = enterprise.get('question_6')
            question_7 = enterprise.get('question_7')
            question_8 = enterprise.get('question_8')
            question_9 = enterprise.get('question_9')
            question_10 = enterprise.get('question_10')
            question_11 = enterprise.get('question_11')
            question_12 = enterprise.get('question_12')
            question_13 = enterprise.get('question_13')
            question_14 = enterprise.get('question_14')
            question_15 = enterprise.get('question_15')
            nps = enterprise.get('nps')

            enterprise_to_add = RepositoryEnterprise.update(
                id,
                name, 
                question_1, 
                question_2,
                question_3,
                question_4,
                question_5,
                question_6,
                question_7,
                question_8,
                question_9,
                question_10,
                question_11,
                question_12,
                question_13,
                question_14,
                question_15,
                nps
            )
            return enterprise_to_add
        except Exception as ex:            
            error = "Enteprise Service - update_enterprise error: {}".format(ex)
            raise Exception(error)
