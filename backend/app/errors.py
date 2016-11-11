from app import app
from flask import logging
from flask import render_template


@app.errorhandler(Exception)
def default_errorhandler(error):
    logger = logging.getLogger('root')
    logger.error(error)
    return render_template('errors/default.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')
