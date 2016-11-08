from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, DataRequired, Length, Regexp, EqualTo, ValidationError

from .models import User


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                         'Usernames must have only letters, '
                                                                                         'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(login=field.data).first():
            raise ValidationError('Username already in use.')