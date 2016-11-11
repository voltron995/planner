from flask.views import MethodView
from flask import flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

from app import app, db, login_manager

from app.email import send_email

from .tokens import Token
from .forms import LoginForm, RegisterForm, ResendForm
from .models import User

HOME_PAGE = 'events.list'

@login_manager.user_loader
def load_user(uuid):
    return User.query.filter_by(uuid=uuid).first()


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('users.login'))


class UsersLogin(MethodView):
    def get(self):
        1/0
        if current_user.is_authenticated:
            return redirect(url_for(HOME_PAGE))
        return render_template('users/login.html', form=LoginForm())

    def post(self):
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            login_user(user)
            return redirect(request.args.get('next') or url_for(HOME_PAGE))
        form.flash_errors()
        return redirect(url_for('users.login'))


class UsersLogout(MethodView):
    @login_required
    def post(self):
        logout_user()
        return redirect(url_for('.login'))


class UsersRegister(MethodView):
    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for(HOME_PAGE))
        return render_template('users/register.html', form=RegisterForm())

    def post(self):
        form = RegisterForm()

        if form.validate_on_submit():
            user = User(login=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            token = Token.encrypt_confirmation_token(user.uuid)
            send_email(user.email, 'Account Confirmation', 'confirmation', username=user.login, token=token)
            flash("The confirmation letter has been sent to you via email.")
            return redirect(url_for('users.login'))
        form.flash_errors()
        return redirect(url_for('users.register'))


class UsersConfirm(MethodView):
    def get(self, token):
        if current_user.is_authenticated:
            return redirect(url_for(HOME_PAGE))
        uuid = Token.decrypt_confirmation_token(token)
        if uuid:
            user = User.query.filter_by(uuid=uuid).first()
            if user:
                if user.is_active:
                    return redirect(url_for(HOME_PAGE))
                user.is_active = True
                db.session.commit()
                flash('You have confirmed your account. Thanks! You can log in now.')
                return redirect(url_for('users.login'))
        flash('The confirmation link is invalid or has expired.')
        return redirect(url_for('users.resend'))


class UsersResend(MethodView):
    def get(self):
        if current_user.is_authenticated:
            return redirect(HOME_PAGE)
        return render_template('users/resend.html', form=ResendForm())

    def post(self):
        form = ResendForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            token = Token.encrypt_confirmation_token(user.id)
            send_email(user.email, 'Account Confirmation', 'confirmation', username=user.login, token=token)
            flash("The new confirmation letter has been sent to you via email.")
            return redirect(url_for('users.login'))
        form.flash_errors()
        return redirect(url_for(HOME_PAGE))
