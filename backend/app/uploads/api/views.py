from flask import request
from flask import send_file
from flask.views import MethodView

from app.api import response
from app.uploads.api.schemas import UploadSchema
from app.uploads.uploads_manager import UploadsManager


class UploadView(MethodView):
    def post(self):
        file = request.files['file']
        data = UploadsManager.save_tmp_file(file)
        return response.success(data=data, schema=UploadSchema)


class DownloadView(MethodView):
    def get(self, group, file_uuid):
        file = UploadsManager.get_file(file_uuid, group)
        return send_file(file.path, mimetype='image/jpeg')
