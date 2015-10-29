from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorschoose'
COLLECTION_NAME = 'projects'
FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donorschoose/projects")
def donorschoose_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=1000)
    #projects = collection.find(projection=FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

DBS_NAME2 = 'sensing'
COLLECTION_NAME2 = 'g1'
FIELDS2 = {'cellid': True, 'channel': True, 'sector': True, 'date': True, 'sensor': True, '_id': False}

@app.route("/sensingplatform/collection")
def sensingplatform_collection():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME2][COLLECTION_NAME2]
    projects = collection.find(projection=FIELDS2, limit=50)
    #projects = collection.find(projection=FIELDS)
    json_projects2 = []
    for project in projects:
        json_projects2.append(project)
    json_projects2 = json.dumps(json_projects2, default=json_util.default)
    connection.close()
    return json_projects2


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)