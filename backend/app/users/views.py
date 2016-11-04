from flask.views import MethodView
from flask import render_template, request

from .forms import LoginForm


class UsersLogin(MethodView):

    def get(self):
        form = LoginForm()
        return render_template('users/login.html', form=form)

    def post(self):
        return 'post'
