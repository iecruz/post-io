from flask import Flask, render_template, request, url_for, jsonify
from flask_socketio import SocketIO, send, emit
from core import api, models, posts

import time
import json

app = Flask(__name__)

app.config.from_object('core.config')
app.register_blueprint(api.app, url_prefix='/api')
app.register_blueprint(posts.app)

socketio = SocketIO(app)

@socketio.on('connect')
def connect_server():
    models.initialize_db()

@socketio.on('disconnect')
def connect_server():
    models.close_db()

@socketio.on('message')
def handle_message(message):
    send(message)

@socketio.on('request_load')
def request_post(message):
    emit('response_load', api.get_post_socket())

@socketio.on('create_post')
def create_post(message):
    if api.create_post_socket(message):
        print(message)
        emit('insert_post', json.loads(json.dumps(message)), broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
