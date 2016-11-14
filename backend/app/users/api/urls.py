from app.users.api import permitters
from . import api_users, api_profiles
from . import views, validators

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
