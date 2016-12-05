from app.error_handlers.errors import InvalidAttribute

from app import app
from app.api.validators import Validator
from app.error_handlers.exceptions import APIBadRequest


class UploadValidator(Validator):
    def post(self):
        if 'file' not in self._request.files:
            raise APIBadRequest(InvalidAttribute('File attribute is required.'))

        file = self._request.files['file']

        if not file.filename.strip():
            raise APIBadRequest(InvalidAttribute('File name could not be empty.'))

        if file.mimetype.replace('image/', '') not in app.config['ALLOWED_EXTENSIONS']:
            raise APIBadRequest(InvalidAttribute('Not allowed file type.'))


class DownloadValidator(Validator):
    def get(self):
        # todo: do we need to validate something?
        pass

