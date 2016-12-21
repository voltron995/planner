from flask import flash, redirect, render_template, url_for
from flask.views import MethodView
from flask_login import current_user, login_user, logout_user, login_required

from app import db, login_manager
from app.error_handlers.error_handlers import mail_logger
from app.mail import send_email
from .forms import LoginForm, RegisterForm, ResendForm
from .models import User, Profile
from .tokens import Token

HOME_PAGE = 'home'


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('users.login'))


class UsersLogin(MethodView):
    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for(HOME_PAGE))
        return render_template('users/login.html', form=LoginForm())

    def post(self):
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            login_user(user)
            return redirect(url_for(HOME_PAGE))
        form.flash_errors()
        return redirect(url_for('users.login'))


class UsersRegister(MethodView):
    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for(HOME_PAGE))
        return render_template('users/register.html', form=RegisterForm())

    def post(self):
        form = RegisterForm()

        if form.validate_on_submit():
            user = User(login=form.username.data, email=form.email.data, password=form.password.data)
            user.profile = Profile()
            db.session.add(user)
            db.session.commit()
            token = Token.encrypt_confirmation_token(user.id)
            send_email(user.email, 'Account Confirmation', 'confirmation', username=user.login, token=token)
            mail_logger.info('Confirmation token {} has been sent to {}'.format(token, user.email))
            flash('The confirmation letter has been sent to you via email.')
            return redirect(url_for('users.login'))
        form.flash_errors()
        return redirect(url_for('users.register'))


class UsersConfirm(MethodView):
    def get(self, token):
        if current_user.is_authenticated:
            return redirect(url_for(HOME_PAGE))
        id = Token.decrypt_confirmation_token(token)
        if id:
            user = User.query.get(id)
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
        # if current_user.is_authenticated:
            # return redirect(url_for(HOME_PAGE))
        return render_template('users/resend.html', form=ResendForm())

    def post(self):
        form = ResendForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            token = Token.encrypt_confirmation_token(user.id)
            send_email(user.email, 'Account Confirmation', 'confirmation', username=user.login, token=token)
            mail_logger.info('Confirmation token {} has been sent to {} one more time.'.format(token, user.email))
            flash('The new confirmation letter has been sent to you via email.')
            return redirect(url_for('users.login'))
        form.flash_errors()
        return redirect(url_for(HOME_PAGE))
