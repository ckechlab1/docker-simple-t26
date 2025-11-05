# pip install flask
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

details = {
    "ann" : {"id": "123", "dept": "IT"},
    "john" : {"id": "456", "dept": "HR"}
}

@app.route('/')
def index():
    return jsonify({'name': 'REST API example in Python',
                    'version': 'demo 1'})

@app.route('/search', methods=['GET'])
def search():
    args = request.args
    if "name" in args:
        argsasdict = args.to_dict()
        name_to_search = argsasdict["name"].lower()
        # return "will search for ", name_to_search, args
        # return details[name_to_search]
        # return str(name_to_search in details)
        if name_to_search in details: 
            return details[name_to_search]
        else:
            return f"Name: {name_to_search} not found"
    else:
        return "Please pass a name to look up. Eg. /search?name=Ck"

app.run()