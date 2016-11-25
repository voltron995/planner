from app.uploads.api import api_uploads
from app.uploads.api.permitters import UploadPermitter, DownloadPermitter
from app.uploads.api.views import UploadView, DownloadView

api_uploads.add_url_rule(
    '/',
    view_func=UploadView.as_view('upload'),
    permitter=UploadPermitter,
)


api_uploads.add_url_rule(
    '/<group>/<file_uuid>',
    view_func=DownloadView.as_view('download'),
    permitter=DownloadPermitter,
)
