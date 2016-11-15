from flask import jsonify

from app.api.schemas import ErrorSchema


def success(data, schema=None, meta=None, many=False):
    if schema:
        data, _ = schema().dump(data, many=many)

    data = {'data': data}

    if meta:
        data['meta'] = meta

    return response(data=data, status=200)


def error(status: int, *errors):
    data, _ = ErrorSchema().dump(errors, many=True)
    data = {'errors': data}
    return response(data=data, status=status)


def response(data: dict, status: int) -> object:
    resp = jsonify(data)
    resp.status_code = status
    return resp
