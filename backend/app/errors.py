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
