import os
import re
from os.path import join, isfile, splitext
from smtplib import SMTPException

from flask import render_template
from flask import request

from app import app
from app.api import response
from app.error_handlers.errors import logger, Error
from app.error_handlers.exceptions import APIExceptions, APIException


def get_templates():
    template_path = join(app.root_path, app.template_folder, 'errors/')
    files = [splitext(f)[0] for f in os.listdir(template_path) if isfile(join(template_path, f))]
    return [int(f) for f in files if f.isdigit()]


def http_error_handler(error):
    if re.match(r'/api', request.path):
        return api_error_handler(APIExceptions.get(error.code, APIException)())
    if error.code in get_templates():
        return render_template('errors/{}.html'.format(error.code))
    return render_template('errors/default.html')


def api_error_handler(exception):
    if not issubclass(exception.__class__, APIException):
        error = Error(detail=str(exception))
        exception = APIException()
        exception.add_error(error)

    return response.error(exception.status, *exception.errors)


@app.errorhandler(Exception)
def default_errorhandler(error):
    logger.error(error)
    if re.match(r'/api', request.path):
        return api_error_handler(APIExceptions.get(error.code, APIException)())
    return render_template('errors/default.html')


@app.errorhandler(SMTPException)
def mail_error(error):
    logger.error(error)
    return render_template('errors/email.html')
