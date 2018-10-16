#coding:utf-8
#download
from flask import Blueprint, render_template, redirect, jsonify
from os import listdir
from os.path import join, isdir, exists
download = Blueprint('download',__name__)

# @user.route('/index')
# def index():
#     return render_template('user/index.html')
# @user.route('/add')
# def add():
#     return 'user_add'
# @user.route('/show')
# def show():
#     return 'user_show'

@download.route('/listdir/<path:rootDir>/<int:idx>')
def list_dir(rootDir, idx=1):
    # rootDir = path
    rootDir = rootDir.replace('$','/')
    if not exists(rootDir):
        return jsonify([{}])
    # idx = 1
    # idx = int(idx)
    if idx == 1:
        response = {
            'listdir': [{'id':idx,'label':rootDir,'children':[]}]
        }
        c = response['listdir'][0]['children']
    else:
        response = {'listdir':[]}
        c = response['listdir']
    folder = []
    files = []
    for lists in listdir(rootDir):
        path = join(rootDir, lists)
        if isdir(path):
            folder.append(lists)
        else:
            files.append(lists)

    for f in folder:
        idx += 1
        c.append({
            'id': idx,
            'label': f,
            'children':[]
        })

    for f in files:
        idx += 1
        c.append({
            'id': idx,
            'label': f
        })
    return jsonify(response)