from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)



class HelloWorld(Resource):
    
    def get(self):
        root = 'hellah'
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

    
    










