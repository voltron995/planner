from app.error_handlers.errors import Error
from flask import request
from flask.views import MethodView

from app.api import response
from app.error_handlers.exceptions import APIBadRequest
from app.uploads.api.schemas import UploadSchema
from app.uploads.manager import UploadsManager
from app.uploads.validators import get_validator


class UploadView(MethodView):
    def post(self, group: str):
        if 'file' not in request.files:
            raise APIBadRequest(Error(detail='File attribute is required.'))

        file = request.files['file']
        get_validator(group)(file).validate()

        data = UploadsManager.save_tmp_file(file)

        return response.success(data=data, schema=UploadSchema)
