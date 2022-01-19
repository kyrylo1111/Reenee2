from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kiril:Zakyta1941@localhost/Main'
app.config['WHOOSH_BASE'] = 'whoosh'
db = SQLAlchemy(app)
db.init_app(app)
api = Api(app)

with app.app_context():
    from routes.todo import *

if __name__ == '__main__':
    app.run(debug=True)





