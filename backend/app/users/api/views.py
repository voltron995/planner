from flask import jsonify
from flask.views import MethodView


class UserSingle(MethodView):
    def get(self, user_id):
        user = {
            'id': user_id,
            'attributes': {
                'name': 'Vasya!',
            }
        }

        return jsonify(data=user)
