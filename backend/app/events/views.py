from flask.views import MethodView
from flask import render_template, request


class EventsList(MethodView):

    def get(self):
        return render_template('events/list.html')

    def post(self):
        return 'post'

    def delete(self):
        return 'delete'

    def put(self):
        return 'put'


class EventsSingle(MethodView):

    def get(self, event_id):
        return render_template('events/single.html')

    def post(self, event_id):
        return 'post' + event_id

    def delete(self, event_id):
        return 'delete' + event_id

    def put(self, event_id):
        return 'put' + event_id