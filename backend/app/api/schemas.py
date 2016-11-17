from marshmallow import Schema, fields, pre_load, post_dump

from app.errors import BadRequest
from app.errors import Error


class BaseSchema(Schema):
    _type = ''

    uuid = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @post_dump(pass_many=True)
    def wrap(self, data, many):
        if many:
            data = list(map(
                lambda item: self._item_wrap(item),
                data
            ))
        else:
            data = self._item_wrap(data)
        return data

    def _item_wrap(self, item):
        return {
            'uuid': item.pop('uuid', None),
            'type': self._type,
            'attributes': item
        }

    @pre_load
    def process_input(self, json_input):
        if 'data' not in json_input:
            raise BadRequest(Error('Required DATA member is missing.'))

        data = json_input['data']
        if self._type != data['type']:
            raise BadRequest(Error('Invalid schema type.'))

        if 'uuid' not in data:
            raise BadRequest(Error('Required UUID member is missing.'))

        if 'attributes' not in data:
            raise BadRequest(Error('Required UUID member is missing.'))

        output = data['attributes']

        return output


class ErrorSchema(Schema):
    title = fields.Str(dump_only=True)
    detail = fields.Str(dump_only=True)
    status = fields.Int(dump_only=True)
    source = fields.Str(dump_only=True)
