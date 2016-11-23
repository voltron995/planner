from app import app
from app.api.validators import Validator
from app.errors import BadRequest, InvalidAttribute


class UploadValidator(Validator):
    def post(self):
        if 'file' not in self._request.files:
            raise BadRequest(InvalidAttribute('File attribute is required.'))

        file = self._request.files['file']

        if not file.filename.strip():
            raise BadRequest(InvalidAttribute('File name could not be empty.'))

        if file.mimetype.replace('image/', '') not in app.config['ALLOWED_EXTENSIONS']:
            raise BadRequest(InvalidAttribute('Not allowed file type.'))


class DownloadValidator(Validator):
    def get(self):
        # todo: do we need to validate something?
        pass

