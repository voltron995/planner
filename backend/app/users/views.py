from flask.views import MethodView
from flask import redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import db, login_manager

from .forms import LoginForm
from .models import User


class UsersLogin(MethodView):

    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for('events.list'))
        return render_template('users/login.html', form=LoginForm())

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user)
                return redirect(url_for('events.list'))
            return 'no such user'
        return 'not valid'


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
