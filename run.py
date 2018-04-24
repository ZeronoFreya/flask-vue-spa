from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
import requests
import os

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/listdir')
def list_dir():
    rootDir = 'e:/Fonts/'
    response = {
        'listdir': []
    }
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        # if os.path.isdir(path):
        #     Test3(path, level+1)
        response['listdir'].append(path)
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
