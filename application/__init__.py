from flask import Flask
from flask_restful import Api

from application.app import Users, User
from application.db import init_db


def create_app(config_file):
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(config_file)

    init_db(app)

    api.add_resource(Users, '/users')
    api.add_resource(User, '/user', '/user/<string:cpf>')
    return app
