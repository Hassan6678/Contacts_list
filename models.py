from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///list.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

class Contact(database.Model):

    __tablename__ = 'contacts'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), nullable=True, unique=True)
    firstname = database.Column(database.String(50), nullable=True)
    lastname = database.Column(database.String(50), nullable=False)
    phone = database.Column(database.String(20), nullable=True, unique=False)
    # Defining One to Many relationships with the relationship function on the Parent Table
    email = database.relationship('Email', backref='contacts', lazy=True, cascade="all, delete-orphan")

    created_at = database.Column(database.DateTime, server_default=database.func.now())
    updated_at = database.Column(database.DateTime, onupdate=database.func.now())

    def __repr__(self):
        return '<Contacts %r>' % self.firstname


class Email(database.Model):

    __tablename__ = 'e_mail'

    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(80), nullable=False, unique=True)
    contact_id = database.Column(database.Integer, database.ForeignKey("contacts.id"),nullable=False)

    def __repr__(self):
        return '<Email %r>' % self.email