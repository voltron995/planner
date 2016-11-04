from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email


class LoginForm(FlaskForm):

    email = EmailField('Email', validators=[Email()])
    password = PasswordField('Password')
    submit = SubmitField('Log In')
