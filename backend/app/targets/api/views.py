from flask import jsonify
from flask.views import MethodView


class TargetsList(MethodView):
    def get(self):
        targets = [
            {'id': 1, 'name': 'Lose weight!', 'status': 'in progress'},
            {'id': 2, 'name': 'Gain weight', 'status': 'achieved'},
            {'id': 3, 'name': 'Balanced nutrition', 'status': 'failed'},

        ]
        return jsonify(data=targets)


class TargetsSingle(MethodView):
    def get(self, target_id):
        target = {
            'id': target_id,
            'attributes': {
                'name': 'Lose weight!',
                'status': 'in progress'
            }
        }

        return jsonify(data=target)