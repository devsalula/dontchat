import os

from flask import Flask
from flask_pymongo import PyMongo

from project.api.controller import controller_blueprint


db = PyMongo()


def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + \
        os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + \
        ':27017/' + os.environ['MONGODB_DATABASE']

    db.init_app(app)

    app.register_blueprint(controller_blueprint)

    return app