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
    }])

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
    }])

    # pergjigjen e kthyer dhe te konvertuar ne JSON ne baze te json_util.dumps() e ruajme ne resp
    resp = Response(
        response=json_util.dumps(json['result']),
        mimetype='application/json')

    # ne momentin kur hapim  
    return resp
    
    
    
@app.route("/q5/<string:municipality>")
def q5(municipality):
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
            "q5a1" : { 
                "$sum": "$q5.answers.a1.value" 
            }, 
            "q5a2" : { 
                "$sum": "$q5.answers.a2.value" 
            }, 
            "q5a3" : { 
                "$sum": "$q5.answers.a3.value" 
            }, 
            "q5a4" : { 
                "$sum": "$q5.answers.a4.value" 
            }, 
            "q5a5" : { 
                "$sum": "$q5.answers.a5.value" 
            }, 
            "q5a6" : { 
                "$sum": "$q5.answers.a6.value" 
            }, 
        }
    }])

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
