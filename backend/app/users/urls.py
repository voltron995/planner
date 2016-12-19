from . import users_blueprint
from . import views

users_blueprint.add_url_rule('/login', view_func=views.UsersLogin.as_view('login'))
users_blueprint.add_url_rule('/register', view_func=views.UsersRegister.as_view('register'))
users_blueprint.add_url_rule('/confirm/<token>', view_func=views.UsersConfirm.as_view('confirm'))
users_blueprint.add_url_rule('/resend', view_func=views.UsersResend.as_view('resend'))
