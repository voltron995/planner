from .. import module
from . import views

module.add_url_rule('/<ms_name>/<action>', view_func=views.MsClient.as_view('msclient'))
