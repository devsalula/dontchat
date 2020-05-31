import json
import time

from flask import Blueprint, redirect, url_for, render_template
from flask_socketio import join_room, leave_room, emit
from flask_mail import Message

from project import socketio, db, email_sender, mail

socket_blueprint = Blueprint('socket', __name__)

@socketio.on('joined')
def handle_connect(data):
    room = data['chatId']
    join_room(room)
    emit('join_room', data, room=room)

@socketio.on('message')
def handle_message(data):
    convert = json.dumps(data)
    load_data = json.loads(convert)
    db.messages.insert_one(load_data)
    emit('message', data, broadcast=True, room=data['chatId'])

@socketio.on('send_email')
def handle_email(data):
    messages = get_messages_by_chat_id(data['chatId'])
    email_receiver = data['email']
    msg = Message(subject="Histórico de Conversas", sender=email_sender, recipients=[email_receiver], body=messages)  
    mail.send(msg)
    emit('bye', data, broadcast=True, room=data['chatId'])

def get_messages_by_chat_id(chat_id):    
    values = db.messages.find({'chatId': chat_id})
    messages = 'Sala ' + chat_id + '\n'
    for document in values:
        message = document['username'] + ': ' + document['message'] + ' às ' + document['date'] + '\n'
        messages += message
    return messages