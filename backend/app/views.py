from flask import render_template
from flask_login import login_required
from flask.views import MethodView


class FrontendAppView(MethodView):
    @login_required
    def get(self, path=None):
        return render_template('layouts/angular.html')
