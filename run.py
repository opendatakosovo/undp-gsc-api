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
	{"$project": {
		"_id":0,
		"1": {
			"a":"$q1a1",
			"b": "$q1a2",
            "c": "$q1a3",
            "d": "$q1a4",
            "e": "$q1a5",
            "f": "$q1a6",
            "g": "$q1a7",
            "h": "$q1a8",
            "i": "$q1a9",
            "j": "$q1a10",
            "k": "$q1a11",
            "l": "$q1a12"            		}
	}
	}
])

    # pergjigjen e kthyer dhe te konvertuar ne JSON ne baze te json_util.dumps() e ruajme ne resp
    resp = Response(
        response=json_util.dumps(json['result']),
        mimetype='application/json')

    # ne momentin kur hapim  
    return resp

@app.route("/q2/<string:municipality>")
def q2(municipality):
    '''
        sh.: /q2/Ferizaj
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
    {"$project":{
        "_id": 0,
        "2": {
            "a":"$q2a1",
            "b":"$q2a2",
            "c":"$q2a3",
            "d": "$q2a4",
            "e":"$q2a5",
            "f": "$q2a6"
        }
    }}
    ])

    # pergjigjen e kthyer dhe te konvertuar ne JSON ne baze te json_util.dumps() e ruajme ne resp
    resp = Response(
        response=json_util.dumps(json['result']),
        mimetype='application/json')

    # ne momentin kur hapim  
    return resp
    
    
    
@app.route("/q8/<string:municipality>")
def q8(municipality):
    '''
        sh.: /q5/Ferizaj
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
    {"$project":{ 
        "_id": 0,
        "13":{ 
            "a": "$q13a1",
            "b": "$q13a2",
            "c": "$q13a3",
            "d": "$q13a4",
            "e": "$q13a5",
            "f": "$q13a6",
            "g": "$q13a7",
            "h": "$q13a8",
            "i": "$q13a9",
            "j": "$q13a10"
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
