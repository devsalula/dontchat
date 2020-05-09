import os

from flask import Flask
from flask_pymongo import PyMongo
from flask_socketio import SocketIO


db = PyMongo()
socketio = SocketIO()

app = Flask(__name__)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + \
    os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + \
    ':27017/' + os.environ['MONGODB_DATABASE']

db.init_app(app)
socketio.init_app(app)

from project.api.controller import controller_blueprint
from project.api.socket import socket_blueprint
app.register_blueprint(controller_blueprint)
app.register_blueprint(socket_blueprint)
