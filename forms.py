from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=-1, max=50, message='You cannot have more than 50 characters')])
    firstname = StringField('Firstname', validators=[DataRequired(),Length(min=-1, max=50, message='You cannot have more than 50 characters')])
    lastname = StringField('Lastname', validators=[Length(min=-1, max=50, message='You cannot have more than 50 characters')])
    phone = StringField('Phone', validators=[Length(min=-1, max=20, message='You cannot have more than 20 characters')])


class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])

class AddEmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    contact_id = StringField('Contact_id', validators=[DataRequired(),Length(min=-1, max=50, message='You cannot have more than 50 characters')])

