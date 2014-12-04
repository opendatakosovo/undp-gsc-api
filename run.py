from flask import Flask
from flask import Response
from bson import json_util, SON
from pymongo import MongoClient
import argparse

# krijojme nje objekt te MongoClient(), klase e cila gjendet ne pymongo
mongo = MongoClient()

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
        sh.: /question/1/group/gender
    '''
    number_of_answers = 0

    # Set the number of answers expected for each question
    if qid == 1:
        number_of_answers = 5
    elif qid == 2:
        number_of_answers = 10
    elif qid == 3:
        number_of_answers = 2
    else:
        # TODO: Throw error
        number_of_answers = 20

    # Build $group JSON
    group_json = {}
    group_json["_id"] = "$surveyee." + group

    for answer_index in range(number_of_answers):
        question_key = "q" + str(qid) + "a" + str(answer_index)
        group_json[question_key] = {
            "$sum": "$q" + str(qid) + ".answers.a" + str(answer_index) + ".value"
        }

    # Build $project JSON object
    project_json = {}
    

    for answer_index in range(number_of_answers):
        answer_key = "a" + str(answer_index)
        question_key_ref = "$q" + str(qid) + "a" + str(answer_index)

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
    result_json = db.gsc.aggregate(aggregate_json)

    # Build response object
    resp = Response(
        response=json_util.dumps(result_json['result']),
        mimetype='application/json')

    # Return response
    return resp

@app.route("/q1/<string:municipality>")
def q1(municipality):
    '''
        sh.: /q1/Ferizaj
    '''
    # ruajme rezultatin qe na kthehet nga databaza permes ekzekutimit te kerkeses(Query) ne json.
    json = db.gsc.aggregate([{  
        "$match" : { 
            "surveyee.municipality" : municipality
        } 
    },
    {
        "$group" : { 
            "_id" : { 
            }, 
            "q1a1" : { 
                "$sum": "$q1.answers.a1.value" 
            }, 
            "q1a2" : { 
                "$sum": "$q1.answers.a2.value" 
            }, 
            "q1a3" : { 
                "$sum": "$q1.answers.a3.value" 
            }, 
            "q1a4" : { 
                "$sum": "$q1.answers.a4.value" 
            }, 
            "q1a5" : { 
                "$sum": "$q1.answers.a5.value" 
            }, 
            "q1a6" : { 
                "$sum": "$q1.answers.a6.value" 
            }, 
            "q1a7" : { 
                "$sum": "$q1.answers.a7.value" 
            }, 
            "q1a8" : { 
                "$sum": "$q1.answers.a8.value" 
            }, 
            "q1a9" : { 
                "$sum": "$q1.answers.a9.value" 
            }, 
            "q1a10" : { 
                "$sum": "$q1.answers.a10.value" 
            }, 
            "q1a11" : { 
                "$sum": "$q1.answers.a11.value" 
            }, 
            "q1a12" : { 
                "$sum": "$q1.answers.a12.value" 
            }
        }
    },
    {
            "$project" : {
                "_id" : 0,
                "a1" : "$q1a1",
                "a2" : "$q1a2",
                "a3" : "$q1a3",
                "a4" : "$q1a4",
                "a5" : "$q1a5",
                "a6" : "$q1a6",
                "a7" : "$q1a7",
                "a8" : "$q1a8",
                "a9" : "$q1a9",
                "a10" : "$q1a10",
                "a11" : "$q1a11",
                "a12" : "$q1a12"
            }
        }
    ])


    # pergjigjen e kthyer dhe te konvertuar ne JSON ne baze te json_util.dumps() e ruajme ne resp
    resp = Response(
        response=json_util.dumps(json['result']),
        mimetype='application/json')

    # ne momentin kur hapim  
    return resp
    
@app.route("/q2Gender/<string:municipality>/<string:gender>")
def q2Gender(municipality, gender):
    '''
        sh.: /q2/Ferizaj
    '''
    # ruajme rezultatin qe na kthehet nga databaza permes ekzekutimit te kerkeses(Query) ne json.
    json = db.gsc.aggregate([{
        "$match" : {
            "surveyee.municipality" : municipality,
            "surveyee.gender": gender
        }
    },
    {
        "$group" : {
            "_id" : {
            },
            "q2a1" : {
                "$sum": "$q2.answers.a1.value"
            },
            "q2a2" : {
                "$sum": "$q2.answers.a2.value"
            },
            "q2a3" : {
                "$sum": "$q2.answers.a3.value"
            },
            "q2a4" : {
                "$sum": "$q2.answers.a4.value"
            },
            "q2a5" : {
                "$sum": "$q2.answers.a5.value"
            },
            "q2a6" : {
                "$sum": "$q2.answers.a6.value"
            }
        }
    },
    {
	"$project": {
            "_id": 0,
		    "a1": "$q2a1",
		    "a2": "$q2a2",
		    "a3": "$q2a3",
		    "a4": "$q2a4",
		    "a5": "$q2a5",
	        "a6": "$q2a6"
     	}
     }])

    # pergjigjen e kthyer dhe te konvertuar ne JSON ne baze te json_util.dumps() e ruajme ne resp
    resp = Response(
        response=json_util.dumps(json['result']),
        mimetype='application/json')

    # ne momentin kur hapim
    return resp


@app.route("/q2age/<string:municipality>/<int:ageto>/<int:agefrom>")
def q2a20_29(municipality, ageto, agefrom):
    '''
    '''
    # ruajme rezultatin qe na kthehet nga databaza permes ekzekutimit te kerkeses(Query) ne json.
    json = db.gsc.aggregate([{
        "$match" : {
            "surveyee.municipality": municipality,
            "surveyee.age.to": {"$gte": ageto},
            "surveyee.age.from": {"$lte": agefrom}
        }
    },
    {
        "$group" : {
            "_id" : {

            },
            "q2a1" : {
                "$sum": "$q2.answers.a1.value"
            },
            "q2a2" : {
                "$sum": "$q2.answers.a2.value"
            },
            "q2a3" : {
                "$sum": "$q2.answers.a3.value"
            },
            "q2a4" : {
                "$sum": "$q2.answers.a4.value"
            },
            "q2a5" : {
                "$sum": "$q2.answers.a5.value"
            },
            "q2a6" : {
                "$sum": "$q2.answers.a6.value"
            }
        }
    },
    {
	"$project": {
            "_id": 0,
		    "a1": "$q2a1",
		    "a2": "$q2a2",
		    "a3": "$q2a3",
		    "a4": "$q2a4",
		    "a5": "$q2a5",
	        "a6": "$q2a6"
     	}
     }])

    # pergjigjen e kthyer dhe te konvertuar ne JSON ne baze te json_util.dumps() e ruajme ne resp
    resp = Response(
        response=json_util.dumps(json['result']),
        mimetype='application/json')

    # ne momentin kur hapim
    return resp



@app.route("/q8/<string:municipality>")
def q8(municipality):
    '''
        sh.: /q8/Ferizaj
    '''
    # ruajme rezultatin qe na kthehet nga databaza permes ekzekutimit te kerkeses(Query) ne json.
    json = db.gsc.aggregate([{  
        "$match" : { 
            "surveyee.municipality" : municipality
        } 
    },
    {
        "$group" : { 
            "_id" : {
            }, 
            "q8a1" : { 
                "$sum": "$q8.answers.a1.value" 
            }, 
            "q8a2" : { 
                "$sum": "$q8.answers.a2.value" 
            }, 
            "q8a3" : { 
                "$sum": "$q8.answers.a3.value" 
            }, 
            "q8a4" : { 
                "$sum": "$q8.answers.a4.value" 
            }, 
            "q8a5" : { 
                "$sum": "$q8.answers.a5.value" 
            }, 
            "q8a6" : { 
                "$sum": "$q8.answers.a6.value" 
            } 
        }
    },
     {
	"$project": {
	    "_id" : 0,
	    "8" : { 
		    "d": "$q8a4",
		    "e": "$q8a5",
		    "f": "$q8a6",
		    "a": "$q8a1",
		    "b": "$q8a2",
	            "c": "$q8a3"
		   } 
     	}
     }
])

    # pergjigjen e kthyer dhe te konvertuar ne JSON ne baze te json_util.dumps() e ruajme ne resp
    resp = Response(
        response=json_util.dumps(json['result']),
        mimetype='application/json')

    # ne momentin kur hapim  
    return resp

@app.route("/q13/<string:municipality>")
def q13(municipality):
    '''
        sh.: /q13/Ferizaj
    '''
    # ruajme rezultatin qe na kthehet nga databaza permes ekzekutimit te kerkeses(Query) ne json.
    json = db.gsc.aggregate([{  
        "$match" : { 
            "surveyee.municipality" : municipality
        } 
    },
    { 
        "$group" : { 
            "_id" : { 
            }, 
            "q13a1" : { 
                "$sum": "$q13.answers.a1.value" 
            }, 
            "q13a2" : { 
                "$sum": "$q13.answers.a2.value" 
            }, 
            "q13a3" : { 
                "$sum": "$q13.answers.a3.value" 
            }, 
            "q13a4" : { 
                "$sum": "$q13.answers.a4.value" 
            },
            "q13a5" : {
                "$sum": "$q13.answers.a5.value" 
            }, 
            "q13a6" : { 
                "$sum": "$q13.answers.a6.value" 
            }, 
            "q13a7" : { 
                "$sum": "$q13.answers.a7.value" 
            }, 
            "q13a8" : { 
                "$sum": "$q13.answers.a8.value" 
            }, 
            "q13a9" : { 
                "$sum": "$q13.answers.a9.value" 
            }, 
            "q13a10" : { 
                "$sum": "$q13.answers.a10.value" 
            }
        }
    },
        {
            "$project" : {
                "_id" : 0,
                "a1" : "$q13a1",
                "a2" : "$q13a2",
                "a3" : "$q13a3",
                "a4" : "$q13a4",
                "a5" : "$q13a5",
                "a6" : "$q13a6",
                "a7" : "$q13a7",
                "a8" : "$q13a8",
                "a9" : "$q13a9",
                "a10" : "$q13a10"
            }
        }
])

    # pergjigjen e kthyer dhe te konvertuar ne JSON ne baze te json_util.dumps() e ruajme ne resp
    resp = Response(
        response=json_util.dumps(json['result']),
        mimetype='application/json')

    # ne momentin kur hapim  
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
