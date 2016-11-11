from flask import render_template
from flask_mail import Message

from app import app, mail


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template('email/' + template + '.txt', **kwargs)
    msg.html = render_template('email/' + template + '.html', **kwargs)
    mail.send(msg)
