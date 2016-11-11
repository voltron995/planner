from flask_inputs import Inputs

from app.api import ApiKeyValidation


class EventListInputs(Inputs, ApiKeyValidation):
    pass
