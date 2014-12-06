from flask import Response
from flask.views import View
from bson import json_util

from ugca import utils
from ugca import mongo


class GroupedAnswers(View):

    def dispatch_request(self, qid, group):
        '''Get the answers to a question grouped by a given interviewee parameter
        :param qid: the question id, i.e. the number of the question.
        :param group: which interview parameter to group by:
                        income, gender, municipality , maritalstatus, gender, age, education, region,
                        ethnicity, employment.position, employment.institution, and employtment.level

        sh.: /question/1/group/gender
        sh.: /question/1/group/employment.level
        '''

        result_json = {}

        # Figure out the numer of possible answers for the given question.
        number_of_answers = utils.get_number_of_answers(qid)

        if number_of_answers > 0:

            # Build $group JSON
            group_json = {}
            group_json["_id"] = str("$surveyee." + group)

            for answer_index in range(1, number_of_answers + 1):
                question_key = "q" + str(qid) + "a" + str(answer_index)
                group_json[question_key] = {
                    "$sum": "$q" + str(qid) + ".answers.a" + str(answer_index) + ".value"
                }

            # Build $project JSON object
            project_json = {}

            for answer_index in range(1, number_of_answers + 1):
                question_key = "q" + str(qid)
                answer_key = "a" + str(answer_index)

                question_key_ref = "$" + question_key + "a" + str(answer_index)

                project_json[answer_key] = question_key_ref

            # Build $sort JSON object
            sort_json = {}
            sort_json["_id"] = 1

            # Build aggregate JSON
            aggregate_json = [
                {
                    "$group": group_json
                },
                {
                    "$project": project_json
                },
                {
                    "$sort": sort_json
                }
            ]

            print aggregate_json

            print 'YO'

            # Execture aggregate query
            response_json = mongo.db.gsc.aggregate(aggregate_json)
            answers_json = response_json['result']

            print response_json

            print 'YO2'

            print answers_json

            result_json = {
                "count": {
                    "answers": number_of_answers,
                    "group": len(answers_json)
                },
                "answers": answers_json
            }

        # Build response object
        resp = Response(
            response=json_util.dumps(result_json),
            mimetype='application/json')

        # Return response
        return resp
