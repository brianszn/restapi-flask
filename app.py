from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
db = MongoEngine(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': '27017',
    'username': 'root',
    'password': 'root'
}

api = Api(app)

class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    cpf = db.EmailField(required=True)
    birth_data = db.BirthTimeField(required=True)


class HelloWorld(Resource):
    def get(self):
        root = 'hello w0rld b1tch'
        return root


class Users(Resource):
    def __init__(self) -> None:
        self.dic = {1: 'gato', 2: 'cachorro', 3: 'cavalo'}

    def get(self):
        return self.dic


api.add_resource(HelloWorld, '/')
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
