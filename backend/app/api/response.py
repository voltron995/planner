from flask import jsonify

from app.api.schemas import ErrorSchema


def success(data=None, schema=None, many=False):
    if schema:
        data, _ = schema().dump(data, many=many)

    return response(data=data, status=200)


def error(status: int, *errors):
    # todo: group
    data, _ = ErrorSchema().dump(errors, many=True)
    data = {'errors': data}
    return response(data=data, status=status)


def response(data, status):
    """
    :type data: dict|list|None
    :type status: int
    :rtype: object
    """
    return jsonify(data), status
