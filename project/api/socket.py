from flask import Blueprint

from project import socketio

socket_blueprint = Blueprint('socket', __name__)

@socketio.on('connecting')
def handle_connect(data):
    socketio.emit('connecting', data)

@socketio.on('message')
def handle_message(data):
    socketio.emit('message', data, broadcast=True)