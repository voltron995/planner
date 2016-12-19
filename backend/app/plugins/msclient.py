from requests import Response
from requests import request

from app.api.schemas import ErrorSchema
from app.error_handlers.errors import Error


class MSResponse:
    def __init__(self):
        self.ok = True
        self.data = {}
        self.errors = []
        self.status_code = 200


class MSResponseBuilder:
    @classmethod
    def from_response(cls, response: Response):
        output = MSResponse()
        output.ok = response.ok
        output.status_code = response.status_code

        try:
            json = response.json()
        except (ValueError, TypeError):
            output.ok = False
            output.errors.append(Error('Failed to decode JSON object.'))
        else:
            if response.ok:
                output.data = json
            else:
                for error_dump in ErrorSchema().dump(json.get('errors', []), many=True).data:
                    output.errors.append(Error(**error_dump))
        return output

    @classmethod
    def from_exception(cls, exception: Exception):
        output = MSResponse()
        output.ok = False
        output.status_code = 500
        output.errors.append(Error(str(exception)))

        return output


class MSClient:
    @staticmethod
    def send_request(url: str, method='GET', params=None, json=None) -> MSResponse:
        try:
            response = request(method, url, params=params, json=json, headers={'Content-Type': 'application/json'})
            ms_response = MSResponseBuilder.from_response(response)
        except Exception as exception:
            ms_response = MSResponseBuilder.from_exception(exception)

        return ms_response
