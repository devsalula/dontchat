from flask import Blueprint, render_template, request, redirect, url_for

controller_blueprint = Blueprint('controller', __name__)

@controller_blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@controller_blueprint.route('/chat', methods=['GET'])
def chat_redirect():
    chatId = request.args.get('chatId')
    username = request.args.get('username')
    return render_template('chat.html', username=username, chatId=chatId)
