from . import api_targets
from . import views, validators

api_targets.add_url_rule('/', view_func=views.TargetsList.as_view('list'), validator=validators.List)
api_targets.add_url_rule('/<target_uuid>', view_func=views.TargetsSingle.as_view('single'), validator=validators.Single)

