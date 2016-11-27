from app.uploads.api import api_uploads
from app.uploads.api.permitters import UploadPermitter
from app.uploads.api.views import UploadView

api_uploads.add_url_rule(
    '/<group>',
    view_func=UploadView.as_view('upload'),
    permitter=UploadPermitter,
)
