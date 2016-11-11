from flask import flash
from flask_wtf import FlaskForm


class Form(FlaskForm):
    def flash_errors(self):
        for field, errors in self.errors.items():
            for error in errors:
                flash(error)
