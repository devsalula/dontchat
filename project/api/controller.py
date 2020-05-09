from flask import Blueprint, render_template, request

controller_blueprint = Blueprint('controller', __name__)

@controller_blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@controller_blueprint.route('/chat', methods=['GET'])
def chat():
    username = request.args.get('username')
    chatId = request.args.get('chatId')
    return render_template('chat.html', username=username, chatId=chatId)
