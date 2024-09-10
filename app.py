from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
from mongoengine import StringField, Document, EmailField, DateTimeField

app = Flask(__name__)
api = Api(app)
db = MongoEngine(app)

app.config["MONGODB_SETTINGS"] = {
    "db": "users",
    "host": "mongodb",
    "port": 27017,
    "username": "admin",
    "password": "admin"
}


class UserModel(Document):
    cpf = StringField(required=True, unique=True)
    fisrt_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    birth_date = DateTimeField(required=True)


class Users(Resource):
    def get(self):
        return {"user": 1}


class User(Resource):
    def get(self, cpf):
        return {"message": "CPF"}

    def post(self):
        return {"message": "teste"}


api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
