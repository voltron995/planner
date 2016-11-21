from app.targets.api import permitters
from . import api_targets
from . import views, validators

api_targets.add_url_rule('/', view_func=views.TargetsList.as_view('list'), validator=validators.TargetsList, permitter=permitters.List)
api_targets.add_url_rule('/<target_uuid>', view_func=views.TargetSingle.as_view('single'), validator=validators.TargetSingle, permitter=permitters.Single)

