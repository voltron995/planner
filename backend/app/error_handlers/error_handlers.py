import os
import re
from logging import getLogger
from os.path import join, isfile, splitext
from smtplib import SMTPException

from flask import render_template
from flask import request

from app import app
from app.api import response
from app.error_handlers.errors import Error
from app.error_handlers.exceptions import APIExceptions, APIException

api_logger = getLogger('api_logger')
app_logger = getLogger('app_logger')
mail_logger = getLogger('mail_logger')


def get_templates():
    template_path = join(app.root_path, app.template_folder, 'errors/')
    files = [splitext(f)[0] for f in os.listdir(template_path) if isfile(join(template_path, f))]
    return [int(f) for f in files if f.isdigit()]


def http_error_handler(error):
    if re.match(r'/api', request.path):
        return api_error_handler(APIExceptions.get(error.code, APIException)())
    app_logger.exception('{} {}'.format(request.method, request.path))
    if error.code in get_templates():
        return render_template('errors/{}.html'.format(error.code))
    return render_template('errors/default.html')


def api_error_handler(exception):
    app_logger.error('API caught an exception. Check details in api.log.')
    api_logger.exception('{} {}'.format(request.method, request.path))
    if not issubclass(exception.__class__, APIException):
        error = Error(detail=str(exception))
        exception = APIException()
        exception.add_error(error)

    return response.error(exception.status, *exception.errors)


@app.errorhandler(Exception)
def default_error_handler(error):
    if re.match(r'/api', request.path):
        return api_error_handler(error)
    app_logger.exception()
    return render_template('errors/default.html')


@app.errorhandler(SMTPException)
def mail_error(error):
    app_logger.error('A mailer error occurred. Check details in mail.log.')
    mail_logger.exception()
    return render_template('errors/email.html')
