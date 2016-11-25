from app.targets.api import permitters, api_targets
from app.targets.api import views

api_targets.add_url_rule('/', view_func=views.TargetsList.as_view('list'), permitter=permitters.List)
api_targets.add_url_rule('/<id>', view_func=views.TargetSingle.as_view('single'), permitter=permitters.Single)

