from flask import Response
from flask.views import View
from bson import json_util
from ugca import mongo


class SurveyeeDistribution(View):

    def dispatch_request(self, group):
        '''Get the answers types of corruption as they are preceived, witnessed, and participated in.
        :param group: surveyee property to group by.
                        income, gender, municipality , maritalstatus, gender, age, education, region,
                        ethnicity, employment.position, employment.institution, and employtment.level

        sh.: /surveyee/distribution/gender
        '''

        if group in ['position', 'institution', 'level']:
          group = 'employment.' + group

        # aggregate
        aggregate_json = [
          {
            "$group": {
              "_id": "$surveyee." + group,
              "count": {
                "$sum": 1
              }
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