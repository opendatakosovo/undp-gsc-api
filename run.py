from flask import Flask
from flask import Response
from bson import json_util, SON
from pymongo import MongoClient
from utils import Utils
import argparse

# krijojme nje objekt te MongoClient(), klase e cila gjendet ne pymongo
mongo = MongoClient()

# Create utils instance.
utils = Utils()

# ruajme instancen e databazes mongo.gjakova ne db
db = mongo.undp

# krijojme objekt te Flask
app = Flask(__name__)

# krijojme HomePage permes @app.route("/")
@app.route("/")
def index():
    return "<h1>Une jam Nastradini!</h1>"


@app.route("/question/<int:qid>/group/<string:group>")
def grouped_answers(qid, group):
    '''
        Get the answers to a question grouped by a given interviewee parameter
        :param qid: the question id, i.e. the number of the question.
        :param group: which interview parameter to group by:
                        income, gender, municipality , maritalstatus, gender, age, education, region,
                        ethnicity, employment.position, employment.institution, and employtment.level

        sh.: /question/1/group/gender
        sh.: /question/1/group/employtment.level
    '''
    
    result_json = {}

    # Figure out the numer of possible answers for the given question.
    number_of_answers = utils.get_number_of_answers(qid)

    if number_of_answers > 0:

        # Build $group JSON
        group_json = {}
        group_json["_id"] = "$surveyee." + group

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


        # Build aggregate JSON
        aggregate_json = [
            {
                "$group" : group_json
            },
            {
                "$project" : project_json
            }
        ]

        # Execture aggregate query
        response_json = db.gsc.aggregate(aggregate_json)
        result_json = response_json['result']

    # Build response object
    resp = Response(
        response=json_util.dumps(result_json),
        mimetype='application/json')

    # Return response
    return resp


# Run the app
if __name__ == '__main__':

    # Define the arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to: [%(default)s].')
    parser.add_argument('--port', type=int, default='5030', help='Port to listen to: [%(default)s].')
    parser.add_argument('--debug', action='store_true', default=False, help='Debug mode: [%(default)s].')

    # Parse arguemnts and run the app.
    args = parser.parse_args()
    app.run(debug=args.debug, host=args.host, port=args.port)
