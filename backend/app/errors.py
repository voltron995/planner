from smtplib import SMTPException

from app import app
from flask import logging
from flask import render_template

logger = logging.getLogger('root')


@app.errorhandler(Exception)
def default_errorhandler(error):
    logger.error(error)
    return render_template('errors/default.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')


@app.errorhandler(SMTPException)
def mail_error(error):
    logger.error(error)
    return render_template('errors/email.html')


class Error:
    title = 'Server encountered an internal error.'
    detail = 'Server encountered an internal error.'
    status = 503
    source = None

    def __init__(self, title: str = None, detail: str = None, status: int = None, source: str = None) -> None:
        if title is not None:
            self.title = title
        if detail is not None:
            self.detail = detail
        if status is not None:
            self.status = status
        if source is not None:
            self.source = source


class InvalidAttribute(Error):
    title = 'Invalid Attribute'
    detail = 'Invalid Attribute.'
    status = 422


class AccessDenied(Error):
    title = 'Access Denied'
    detail = 'User is not permitted to perform the requested operation.'
    status = 403


class DefaultException(Exception):
    status = 503
    errors = []

    def __init__(self, *errors, status=None):
        super().__init__()
        self.errors = list(errors)
        if status is not None:
            self.status = status

    def add_error(self, error: Error):
        self.errors.append(error)


class Forbidden(DefaultException):
    status = 403


class BadRequest(DefaultException):
    status = 400
