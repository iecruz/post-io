from flask import Flask, render_template, request, url_for, jsonify
from flask_socketio import SocketIO, send, emit
from core import api, models, posts

import eventlet
import time
import json

app = Flask(__name__)

eventlet.monkey_patch()

app.config.from_object('core.config')
app.register_blueprint(api.app, url_prefix='/api')
app.register_blueprint(posts.app)

socketio = SocketIO(app, async_mode='eventlet')

@app.before_request
def before_request():
    models.initialize_db()

@app.teardown_request
def teardown_request(exception):
    models.close_db()

@socketio.on('create_post')
def create_post(message):
    if api.create_post_socket(message):
        print(message)
        emit('insert_post', json.loads(json.dumps(message)), broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
