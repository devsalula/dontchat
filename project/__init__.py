import os

from flask import Flask
from flask_socketio import SocketIO
from flask_pymongo import PyMongo
from flask_mail import Mail

mongo = PyMongo()
socketio = SocketIO()

app = Flask(__name__)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_URI']

app.static_folder = './templates/static'

mongo.init_app(app)
socketio.init_app(app)

db = mongo.db

email_sender = os.environ['EMAIL_USER']

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email_sender,
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}

app.config.update(mail_settings)

mail = Mail(app)

from project.api.controller import controller_blueprint
from project.api.socket import socket_blueprint
app.register_blueprint(controller_blueprint)
app.register_blueprint(socket_blueprint)
