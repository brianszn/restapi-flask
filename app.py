from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from mongoengine import StringField,EmailField,Document, connect
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,  # Tipo inteiro
    'username': 'adm',
    'password': 'adm'
}


user_parser = reqparse.RequestParser()

user_parser.add_argument('name', type=str, required=True, help="Esse campo não pode estar vazio")
user_parser.add_argument('cpf', type=str, required=True, help="Esse campo não pode estar vazio")
user_parser.add_argument('email', type=str, required=True, help="Esse campo não pode estar vazio")


api = Api(app)

connect(
    db=app.config['MONGODB_SETTINGS']['db'],
    host=app.config['MONGODB_SETTINGS']['host'],
    port=app.config['MONGODB_SETTINGS']['port'],
    username=app.config['MONGODB_SETTINGS']['username'],
    password=app.config['MONGODB_SETTINGS']['password']
)


class UserModel(Document):

    name = StringField(required=True)
    cpf = StringField(required=True, unique=True)
    email = EmailField(required=True)


class Users(Resource):

    def get(self):
        
        return 1


class User(Resource):

    def post(self):
        
        data = user_parser.parse_args()
        UserModel(**data).save()

        return {"msg": "Successfully"}, 201
        
        


api.add_resource(Users, '/users')
api.add_resource(User, '/user')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
