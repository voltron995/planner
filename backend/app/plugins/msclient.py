from requests import Response
from requests import request

from app.errors import Error


class MSResponse:
    def __init__(self, response: Response = None, exception: Exception = None):

        self.ok = True
        self.data = {}
        self.errors = []
        self.status_code = 200

        if response is not None:
            self._from_response(response)
        if exception is not None:
            self._from_exception(exception)

    def _from_response(self, response: Response):
        self.ok = response.ok
        self.status_code = response.status_code

        try:
            json = response.json()
        except (ValueError, TypeError):
            self.ok = False
            self.errors.append(Error('Failed to decode JSON object.'))
        else:
            if response.ok:
                self.data = json['data']
            else:
                # todo: could we trust their json structure? Use marshmellow validator.
                for error in json['errors']:
                    self.errors.append(Error(error['title']))

    def _from_exception(self, exception: Exception):
        self.ok = False
        self.status_code = 500
        self.errors.append(Error(str(exception)))


class MSClient:
    @staticmethod
    def send_request(url: str, data=None, method='GET') -> MSResponse:
        try:
            response = request(method, url, json=data, headers={'Content-Type': 'application/json'})
            ms_response = MSResponse(response=response)
        except Exception as exception:
            ms_response = MSResponse(exception=exception)

        return ms_response
