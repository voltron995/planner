from wtforms import SubmitField, PasswordField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, DataRequired, Length, Regexp, EqualTo, ValidationError

from app.form import Form
from .models import User


class LoginForm(Form):
    email = EmailField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Log In')

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user is None:
            self.email.errors.append('User with such email does not exist.')
            return False
        if not user.verify_password(self.password.data):
            self.password.errors.append('Wrong password.')
            return False
        if not user.is_active:
            self.email.errors.append('You have not confirmed you account yet. Follow the link in the email.')
            return False
        return True


class RegisterForm(Form):
    email = EmailField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField(
        'Username',
        validators=[
            DataRequired(), Length(1, 64),
            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')
        ]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), EqualTo('confirm', message='Passwords must match.')]
    )
    confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(login=field.data).first():
            raise ValidationError('Username already in use.')


class ResendForm(Form):
    email = EmailField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('Send email')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if not user:
            raise ValidationError('You haven\'t registered yet.')
        if user.is_active:
            raise ValidationError('Account with this email is already confirmed. Try to log in!')
