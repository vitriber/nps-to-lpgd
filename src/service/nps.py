from tokenize import Number
from repository.enterprise import Enterprise as RepositoryEnterprise
from repository.questionary import Questionary as RepositoryQuestionary
from repository.answer import Answer as RepositoryAnswer
from collections import ChainMap
from util import Util
import json

class NPS:
    def find_nps(answer):
        try:
            answer_data = RepositoryAnswer.get_all()
            questionary_data = RepositoryQuestionary.get_all()

            format_answer_data = {}
            for row in answer_data:
                if row['questionary_id'] not in format_answer_data:
                    questionary_nps_value = list(filter(lambda x:x['id']==row['questionary_id'],questionary_data))
                    format_value = {}
                    format_value['nps_value'] = questionary_nps_value[0]['nps_value']
                    format_value['constant_factor'] = 1
                    format_answer_data[row['questionary_id']] = [
                        format_value
                    ] 
                format_answer_data[row['questionary_id']].append({'question_' + str(row['question_id']) : row['value']})

            format_data = []
            
            for key in format_answer_data:
                format_data.append(dict(ChainMap(*format_answer_data[key])))

            predictedNPS = Util.get_nps(format_data, answer)
            if(predictedNPS):
                return predictedNPS
            return 'Não foi possível realizar o calculo'
        except Exception as ex:            
            error = "Enteprise Service - find_nps error: {}".format(ex)
            raise Exception(error)
