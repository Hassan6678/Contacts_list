from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///list.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

class Contact(database.Model):

    __tablename__ = 'contacts'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), nullable=True)
    firstname = database.Column(database.String(50), nullable=True)
    lastname = database.Column(database.String(50), nullable=False)
    phone = database.Column(database.String(20), nullable=True, unique=False)

    def __repr__(self):
        return '<Contacts %r>' % self.firstname