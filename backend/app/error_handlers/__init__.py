from app import app
from app.error_handlers.error_handlers import http_error_handler
from app.error_handlers.errors import HTTP_ERROR_CODES

for code in HTTP_ERROR_CODES:
    app.register_error_handler(code, http_error_handler)
