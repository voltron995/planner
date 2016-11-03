from . import views
from .. import msclient

msclient.add_url_rule('/<ms_name>/<action>', view_func=views.MsClient.as_view('msclient'))
