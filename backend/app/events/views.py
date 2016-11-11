from flask_login import login_required
from flask.views import MethodView
from flask import render_template, request


class EventsList(MethodView):

    @login_required
    def get(self):
        # fasfsdfsdf
        return render_template('events/list.html')


class EventsSingle(MethodView):

    @login_required
    def get(self, event_id):
        return render_template('events/single.html', event_id=event_id)
