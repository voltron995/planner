from app.users.api import api_profiles, api_users, permitters, validators, views

api_users.add_url_rule(
    '/<user_uuid>',
    view_func=views.UserSingle.as_view('single'),
    permitter=permitters.UserSingle,
    validator=validators.UserSingle
)

api_profiles.add_url_rule(
    '/<profile_uuid>',
    view_func=views.ProfileSingle.as_view('single'),
    validator=validators.ProfileSingle
)
