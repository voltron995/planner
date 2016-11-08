from flask import current_app
from flask.views import MethodView
from flask import flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import db, login_manager

from app.email import send_email

from .tokens import Token
from .forms import LoginForm, RegisterForm
from .models import User


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(error)

class UsersLogin(MethodView):
    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for('events.list'))
        return render_template('users/login.html', form=LoginForm())

    def post(self):
        form = LoginForm()

        if not form.validate_on_submit():
            flash('Invalid password or email.', 'login_error')
            return redirect(url_for('.login'))

        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('User with such password or email does not exist.', 'login_error')
            return redirect(url_for('.login'))

        login_user(user)
        return redirect(request.args.get('next') or url_for('events.list'))


class UsersLogout(MethodView):
    @login_required
    def post(self):
        logout_user()
        return redirect(url_for('.login'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('users.login'))


class UsersRegister(MethodView):
    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for('events.list'))
        return render_template('users/register.html', form=RegisterForm())

    def post(self):
        form = RegisterForm()

        if form.validate_on_submit():
            user = User(login=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Registered a new user")
            t = Token()
            token = t.generate_confirmation_token(user.id)
            send_email(user.email, 'Account Confirmation', 'confirmation', username=user.login, token=token)
            flash("The confirmation letter has been sent to you via email.")
            return redirect(url_for('users.login'))
        flash_errors(form)
        return redirect(url_for('users.register'))

class UsersConfirm(MethodView):
    def get(self, token):
        t = Token()
        id = t.get_key_from_confirmation_token(token)
        if id:
            user = User.query.filter_by(id=id).first()
            if user.is_active:
                return redirect(url_for('events.list'))
            user.is_active = True
            db.session.add(user)
            db.session.commit()
            flash('You have confirmed your account. Thanks! You can log in now.')
            return redirect(url_for('users.login'))
        flash('The confirmation link is invalid or has expired.')
        return redirect(url_for('users.login')) #todo: resend confirmation email