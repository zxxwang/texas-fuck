from flask import Flask
from flask_restx import Api

app = Flask(__name__)

api = Api(
    app,
    title='texas-fuck',
    version='0.0.1',
    description='texas-fuck utils'
)

from flaskr import api_register
api_register.register('flaskr/api')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
