#coding:utf-8
from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
import requests

from backend.download import download

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(download,url_prefix='/api/dl')

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
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
