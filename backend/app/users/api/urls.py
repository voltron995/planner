from app.users.api import api_profiles, api_users, permitters, validators, views

api_users.add_url_rule(
    '/current',
    view_func=views.UserCurrent.as_view('current'),
    permitter=permitters.UserCurrent,
    validator=validators.UserCurrent
)

api_profiles.add_url_rule(
    '/current',
    view_func=views.ProfileCurrent.as_view('current'),
    validator=validators.ProfileCurrent
)
