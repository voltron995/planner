from flask import jsonify
from flask_login import login_required
from flask.views import MethodView


class EventList(MethodView):
    def get(self):
        events = [
            {'id': 11, 'name': 'Wake Up!', 'start_time': 1477904400},
            {'id': 12, 'name': 'Eat', 'start_time': 1477905400},
            {'id': 13, 'name': 'Drink', 'start_time': 1477906400},
            {'id': 14, 'name': 'Sleep', 'start_time': 1477907400},
            {'id': 15, 'name': 'Write Code', 'start_time': 1477908400},
            {'id': 16, 'name': 'Eat', 'start_time': 1477904400},
            {'id': 17, 'name': 'Play Football', 'start_time': 1477909400},
            {'id': 18, 'name': 'Write Code', 'start_time': 1477910400},
            {'id': 19, 'name': 'Sleep', 'start_time': 1477911400},
            {'id': 20, 'name': 'Drink', 'start_time': 1477912400}
        ]
        return jsonify(data=events)


class EventSingle(MethodView):
    def get(self, event_id):
        event = {
            'id': event_id,
            'attributes': {
                'name': 'Wake Up!',
                'start_time': 1477904400
            }
        }

        return jsonify(data=event)
