from flask import Blueprint, session
from flask_socketio import join_room, emit

from project import socketio

socket_blueprint = Blueprint('socket', __name__)

@socketio.on('joined')
def handle_connect(data):
    room = data['chatId']
    join_room(room)
    emit('join_room', data, room=room)

@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True, room=data['chatId'])