from flask_wtf import Form
from wtforms import SubmitField, PasswordField
from wtforms.fields.html5 import EmailField


class LoginForm(Form):

    email = EmailField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Log In')
