from abc import ABCMeta

from PIL import Image
from werkzeug.datastructures import FileStorage

from app.errors import BadRequest, NotFound, Error
from app.uploads import groups


class UploadValidator(metaclass=ABCMeta):
    MIME_TYPES = NotImplementedError  # type: tuple
    MAX_SIZE = NotImplementedError  # type: int

    def __init__(self, file: FileStorage):
        self.file = file

    def validate(self):
        self._validate_mime_type()
        self._validate_max_size()

    def _validate_max_size(self):
        if len(self.file.read()) > self.MAX_SIZE:
            raise BadRequest()

    def _validate_mime_type(self):
        if self.file.mimetype not in self.MIME_TYPES:
            raise BadRequest(Error('Mime type.'))


class ImageValidator(UploadValidator):
    MIME_TYPES = 'image/jpg', 'image/jpeg', 'image/png', 'image/bmp', 'image/gif'
    MAX_SIZE = 1 * 1024 * 1024
    MAX_HEIGHT = 2400
    MAX_WIDTH = 3600

    def __init__(self, file: FileStorage):
        super().__init__(file)
        self.image = Image.open(file)

    def validate(self):
        super().validate()
        self._validate_max_height()
        self._validate_max_width()

    def _validate_max_height(self):
        if self.image.height > self.MAX_HEIGHT:
            raise BadRequest(Error('Max height.'))

    def _validate_max_width(self):
        if self.image.width > self.MAX_WIDTH:
            raise BadRequest(Error('Max width.'))


class ProfileImageValidator(ImageValidator):
    MIME_TYPES = 'image/jpg', 'image/jpeg', 'image/png'
    MAX_SIZE = 100 * 1024
    MAX_HEIGHT = 250
    MAX_WIDTH = 250


# A dictionary with file validators. The key of the dictionary
# is the name of the uploaded file group and the value is the
# validator class.
_validators = {
    groups.PROFILE_IMAGES: ProfileImageValidator
}


def get_validator(group: str) -> UploadValidator.__class__:
    """
    Returns a validator class for a given upload group.
    :param group: str
    :return: UploadValidator
    """
    try:
        return _validators[group]
    except KeyError:
        raise NotFound()
