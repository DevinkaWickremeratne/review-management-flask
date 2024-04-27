import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app, version='1.0', title='Your API Title', description='Your API Description')

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
