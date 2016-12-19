from app.users.api import api_profiles, api_users, permitters, views

api_users.add_url_rule(
    '/current',
    view_func=views.UserCurrent.as_view('current'),
    permitter=permitters.UserCurrent,
)

api_profiles.add_url_rule(
    '/current',
    view_func=views.ProfileCurrent.as_view('current'),
    permitter=permitters.ProfileCurrent,
)

api_users.add_url_rule(
    '/logout',
    view_func=views.UsersLogout.as_view('logout'),
    permitter=permitters.UsersLogout,
)
