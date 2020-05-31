import os

from flask import Flask
from flask_socketio import SocketIO
from flask_pymongo import PyMongo

mongo = PyMongo()
socketio = SocketIO()

app = Flask(__name__)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_URI']

mongo.init_app(app)
socketio.init_app(app)

db = mongo.db

from project.api.controller import controller_blueprint
from project.api.socket import socket_blueprint
app.register_blueprint(controller_blueprint)
app.register_blueprint(socket_blueprint)
