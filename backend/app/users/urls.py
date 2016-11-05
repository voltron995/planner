from . import users_blueprint
from . import views

users_blueprint.add_url_rule('/login', view_func=views.UsersLogin.as_view('login'))
users_blueprint.add_url_rule('/logout', view_func=views.UsersLogout.as_view('logout'))
