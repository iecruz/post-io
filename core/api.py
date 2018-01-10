from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from core.models import *

import json

app = Blueprint('api', __name__)

@app.route('/get_post/', methods=['GET'])
def get_post():
    return jsonify([model_to_dict(post) for post in Post.select().order_by(Post.date.desc())])
    
@app.route('/create_post/', methods=['POST'])
def create_post():
    result = Post.create(
        author='me',
        title=request.form['title'],
        body=request.form['body'],
    )

    if result is None:
        return jsonify({'result': 'error'})
    else:
        return jsonify({'result': 'success'})

def get_post_socket():
    return json.loads(json.dumps([model_to_dict(post) for post in Post.select().order_by(Post.date.desc())], default=str))

def create_post_socket(data):
    result = Post.create(
        author='me',
        title=data['title'],
        body=data['body'],
    )

    return not result is None
    