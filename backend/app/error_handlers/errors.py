HTTP_ERROR_CODES = {
    400:    'Bad Request',
    401:    'Unauthorized',
    403:    'Forbidden',
    404:    'Not Found',
    405:    'Method Not Allowed',
    406:    'Not Acceptable',
    408:    'Request Timeout',
    409:    'Conflict',
    410:    'Gone',
    411:    'Length Required',
    412:    'Precondition Failed',
    413:    'Request Entity Too Large',
    414:    'Request URI Too Long',
    415:    'Unsupported Media Type',
    416:    'Requested Range Not Satisfiable',
    417:    'Expectation Failed',
    418:    'I\'m a teapot',  # see RFC 2324
    422:    'Unprocessable Entity',
    428:    'Precondition Required',  # see RFC 6585
    429:    'Too Many Requests',
    431:    'Request Header Fields Too Large',
    500:    'Internal Server Error',
    501:    'Not Implemented',
    502:    'Bad Gateway',
    503:    'Service Unavailable',
    504:    'Gateway Timeout',
    505:    'HTTP Version Not Supported',
}

class Error:
    code = 500
    detail = 'Server encountered an internal error.'
    source = None

    def __init__(self, title: str = None, detail: str = None, code: int = None, source: str = None) -> None:
        if code is not None:
            self.code = code
        if detail is not None:
            self.detail = detail
        if source is not None:
            self.source = source
        if title is not None:
            self.title = title
        else:
            self.title = HTTP_ERROR_CODES[self.code]


class InvalidAttribute(Error):
    code = 422
    title = 'Invalid Attribute.'


class AccessDenied(Error):
    code = 403
    title = 'User is not permitted to perform the requested operation.'


class ElementNotFound(Error):
    code = 404
    detail = 'The element cannot be found'



