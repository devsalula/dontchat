from flask import Blueprint, jsonify, render_template

controller_blueprint = Blueprint('controller', __name__)

@controller_blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@controller_blueprint.route('/chat', methods=['GET'])
def chat_room():
    return render_template('chat.html')
