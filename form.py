from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

class Form(FlaskForm):
    name = StringField('Name')
    password = PasswordField('Password')
    email = StringField('Email')
    submit = SubmitField('Submit')