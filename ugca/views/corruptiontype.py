from flask import Response
from flask.views import View
from bson import json_util

from ugca import utils
from ugca import mongo


class CorruptionType(View):

    def dispatch_request(self, corruption_type, group):
        '''Get the answers types of corruption as they are preceived, witnessed, and participated in.
        :param group: the type of corruption. e.g. embezzlement, extortion, nepotism
        :param group: which interview parameter to group by:
                        income, gender, municipality , maritalstatus, gender, age, education, region,
                        ethnicity, employment.position, employment.institution, and employtment.level

        sh.: /corruption-type/embezzlement/group/gender
        '''

        answer_index = str(utils.get_corruption_type_index(corruption_type))

        # aggregate
        aggregate_json = [
          {
            "$group": {
              "_id": "$surveyee." + group,
              "q2": {
                "$sum": "$q2.answers.a" + answer_index + ".value"
              },
              "q5": {
                "$sum": "$q5.answers.a" + answer_index + ".value"
              },
              "q8": {
                "$sum": "$q8.answers.a" + answer_index + ".value"
              }
            }
          },
          {
            "$project": {
              "perceived": "$q2",
              "witnessed": "$q5",
              "participated": "$q8"
            }
          },
          {
            "$sort": {
              "_id": 1
            }
          }
        ]

        response_json = mongo.db.gsc.aggregate(aggregate_json)
        answers_json = response_json['result']


        # Build response object
        resp = Response(
            response=json_util.dumps(answers_json),
            mimetype='application/json')

        # Return response
        return resp