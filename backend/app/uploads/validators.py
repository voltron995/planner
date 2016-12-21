from abc import ABC

from PIL import Image
from app.error_handlers.errors import Error, ElementNotFound
from werkzeug.datastructures import FileStorage

from app.error_handlers.exceptions import APINotFound, APIBadRequest
from app.uploads import groups

# A dictionary with file validators. The key of the dictionary
# is the name of the uploaded file group and the value is the
# validator class.
_validators = {}


def register_validator(validator_class):
    """
    :type validator_class: UploadValidator
    """
    _validators[validator_class.UPLOAD_GROUP] = validator_class


def get_validator(group: str):
    """
    Returns a validator class for a given upload group.
    :param group: str
    :return: UploadValidator
    """
    try:
        return _validators[group]
    except KeyError:
        raise APINotFound(ElementNotFound(detail='The validator cannot be found.'))


def register(cls):
    """
    Decorator to register validator.
    :param cls:
    :return:
    """
    if cls.UPLOAD_GROUP:
        register_validator(cls)
    return cls


class UploadValidator(ABC):
    MIME_TYPES = None  # type: tuple
    MAX_SIZE = None  # type: int
    UPLOAD_GROUP = None  # type: str

    def __init__(self, file: FileStorage):
        self.file = file

    def validate(self):
        self._validate_name()
        self._validate_mime_type()
        self._validate_max_size()

    def _validate_name(self):
        if len(self.file.filename.split('.')) < 2:
            raise APIBadRequest()

    def _validate_max_size(self):
        # todo: better way to get file length.
        file_size = len(self.file.read())
        self.file.seek(0)
        if file_size > self.MAX_SIZE:
            raise APIBadRequest()

    def _validate_mime_type(self):
        if self.file.mimetype not in self.MIME_TYPES:
            raise APIBadRequest(Error(detail='Mime type.'))


class ImageValidator(UploadValidator):
    MIME_TYPES = 'image/jpg', 'image/jpeg', 'image/png', 'image/bmp', 'image/gif'
    MAX_SIZE = 1 * 1024 * 1024
    MAX_HEIGHT = 2400
    MAX_WIDTH = 3600

    def __init__(self, file: FileStorage):
        super().__init__(file)
        self.image = Image.open(file)
        file.seek(0)

    def validate(self):
        super().validate()
        self._validate_max_height()
        self._validate_max_width()

    def _validate_max_height(self):
        if self.image.height > self.MAX_HEIGHT:
            raise APIBadRequest(Error(detail='Max height.'))

    def _validate_max_width(self):
        if self.image.width > self.MAX_WIDTH:
            raise APIBadRequest(Error(detail='Max width.'))


@register
class ProfileImageValidator(ImageValidator):
    UPLOAD_GROUP = groups.PROFILE_IMAGES
    MIME_TYPES = 'image/jpg', 'image/jpeg', 'image/png'
    MAX_SIZE = 100 * 1024
    MAX_HEIGHT = 250
    MAX_WIDTH = 250

@register
class DishImageValidator(ImageValidator):
    UPLOAD_GROUP = groups.DISH_IMAGES
    MIME_TYPES = 'image/jpg', 'image/jpeg', 'image/png'
    MAX_SIZE = 500 * 1024
    MAX_HEIGHT = 240
    MAX_WIDTH = 320
