from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):

    email = EmailField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Log In')
