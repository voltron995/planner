from . import api_events
from . import views, validators

api_events.add_url_rule('/<user_id>', view_func=views.UserSingle.as_view('single'), validator=validators.Single)
