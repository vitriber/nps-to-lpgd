from repository.enterprise import Enterprise as RepositoryEnterprise
from repository.question import Question as RepositoryQuestion
from repository.questionary import Questionary as RepositoryQuestionary
from util import Util
import json

class NPS:
    def find_nps(new):
        try:
            questionary_data = RepositoryQuestionary.get_all()
            questionary_ids = [element["id"] for element in questionary_data]

            all_questionary_data = []

            for questionary_id in questionary_ids:
                formated_data = []
                data = RepositoryQuestion.get_all(questionary_id)
                for question_id in data:
                    formated_data.data[question_id] = data[question_id].value
                formated_data.nps = questionary_data[questionary_id].nps
                formated_data.constant_factor = questionary_data[questionary_id].constant_factor
                all_questionary_data.append(formated_data)

            data_json = json.dumps(all_questionary_data)
            predictedNPS = Util.get_nps(data_json, new)
            if(predictedNPS):
                return predictedNPS
            return 'Não foi possível realizar o calculo'
        except Exception as ex:            
            error = "Enteprise Service - find_nps error: {}".format(ex)
            raise Exception(error)
