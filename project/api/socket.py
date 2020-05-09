from flask import Blueprint

from project import socketio

socket_blueprint = Blueprint('socket', __name__)

@socketio.on('message')
def handle_message(data):
    print(data)