from flask import Blueprint, jsonify, render_template

test_blueprint = Blueprint('ping', __name__)

@test_blueprint.route('/ping', methods=['GET'])
def ping():
    return render_template('index.html')