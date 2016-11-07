from flask.views import MethodView
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import db, login_manager

from app.email import send_email
from .forms import LoginForm, RegisterForm
from .models import User


class UsersLogin(MethodView):

    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for('events.list'))
        return render_template('users/login.html', form=LoginForm())

    def post(self):
        form = LoginForm()

        if not form.validate_on_submit():
            flash('Validation error', 'login_error')
            return redirect(url_for('.login'))

        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('Invalid password or email', 'login_error')
            return redirect(url_for('.login'))

        login_user(user)
        return redirect(url_for('events.list'))


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

