from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, DataRequired, Length


class LoginForm(FlaskForm):

    email = EmailField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Log In')
