from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class ToDo(Resource):
    def get(self):
        return {
            'hello':'world'
        }
    
api.add_resource(ToDo, '/api/v1/todos')


if __name__ == '__main__':
    app.run(debug=True, port=3001)
