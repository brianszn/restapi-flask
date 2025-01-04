from flask import Flask, jsonify
from flask_restful import Resource, Api
from mongoengine import *
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,  # Tipo inteiro
    'username': 'adm',
    'password': 'adm'
}

api = Api(app)

connect(
    db=app.config['MONGODB_SETTINGS']['db'],
    host=app.config['MONGODB_SETTINGS']['host'],
    port=app.config['MONGODB_SETTINGS']['port'],
    username=app.config['MONGODB_SETTINGS']['username'],
    password=app.config['MONGODB_SETTINGS']['password']
)

class UserModel(Document):
    cpf = StringField(required=True, unique=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)


class Users(Resource):
    def get(self):
        return {"message:": "brian"} 
        

class User(Resource):
    def post(self):
        return {"message:": "teste"}
    

api.add_resource(Users, '/users')

api.add_resource(User, '/user', '/user/<string:cpf>')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
