from flask.views import MethodView
from flask import render_template, request
from flask_login import login_user
from .forms import LoginForm
from .models import User
from app import db


class UsersLogin(MethodView):

    def get(self):
        form = LoginForm()
        # new_user = User(email="kate.glebova97@gmail.com", password="pass")
        # db.session.add(new_user)
        # db.session.commit()
        return render_template('users/login.html', form=form)

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None:
                login_user(user)
                return 'login'
            return 'no such user'
        return 'not valid'
