from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
from mongoengine import StringField, Document, EmailField, DateTimeField
from pkg_resources import require

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "db": "users",
    "host": "mongodb",
    "port": 27017,
    "username": "admin",
    "password": "admin"
}

api = Api(app)
db = MongoEngine(app)

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('cpf', type=str, required=True, help="This field cannot be blank")
_user_parser.add_argument('first_name', type=str, required=True, help="This field cannot be blank")
_user_parser.add_argument('last_name', type=str, required=True, help="This field cannot be blank")
_user_parser.add_argument('email', type=str, required=True, help="This field cannot be blank")
_user_parser.add_argument('birth_date', type=str, required=True, help="This field cannot be blank")


class UserModel(Document):
    cpf = StringField(required=True, unique=True)
    first_name = StringField(required=True)
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
        data = _user_parser.parse_args()
        UserModel(**data).save()
        return data


api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
