from flask.views import MethodView
from flask import make_response
import requests


class MsClient(MethodView):

    def get(self, ms_name, action):
        request_str = '{protocol}://{host}:{port}/{uri}/'.format(protocol='http', host='192.168.96.238', port='5000', uri='recipes/5')
        response = requests.get(request_str)
        response = make_response(response.text)
        response.headers['Content-Type'] = 'application/json'
        return response

    def post(self):
        return 'post'

    def delete(self):
        return 'delete'

    def put(self):
        return 'put'