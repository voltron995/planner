from flask import request
from flask import send_file
from flask.views import MethodView

from app import app
from app.api import response
from app.errors import BadRequest, InvalidAttribute
from app.uploads.api.schemas import UploadSchema
from app.uploads.uploads_manager import UploadsManager


class UploadView(MethodView):
    def post(self):
        # todo: upload validation could not be placed inside schema because it is not json
        # todo: figure out where to validate this
        if 'file' not in request.files:
            raise BadRequest(InvalidAttribute('File attribute is required.'))

        file = request.files['file']

        if not file.filename.strip():
            raise BadRequest(InvalidAttribute('File name could not be empty.'))

        if file.mimetype.replace('image/', '') not in app.config['ALLOWED_EXTENSIONS']:
            raise BadRequest(InvalidAttribute('Not allowed file type.'))

        file = request.files['file']
        data = UploadsManager.save_tmp_file(file)
        return response.success(data=data, schema=UploadSchema)


class DownloadView(MethodView):
    # todo: remove GET action. Make nginx serve uploaded files as static.
    def get(self, group, file_uuid):
        file = UploadsManager.get_file(file_uuid, group)
        return send_file(file.path, mimetype='image/jpeg')
