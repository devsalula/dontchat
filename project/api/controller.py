from flask import Blueprint, render_template, request, redirect, url_for

from project import mongo

controller_blueprint = Blueprint('controller', __name__)

@controller_blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@controller_blueprint.route('/chat', methods=['GET'])
def chat_redirect():
    chat_id = request.args.get('chatId')
    username = request.args.get('username')
    return render_template('chat.html', username=username, chatId=chat_id)
