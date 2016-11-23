from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_dump


class UploadSchema(Schema):
    _type = 'uploads'

    uuid = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    group = fields.Str(dump_only=True)
    link = fields.Str(dump_only=True)

    @post_dump(pass_many=True)
    def wrap(self, data, many):
        if many:
            return list(map(lambda item: self._item_wrap(item), data))
        else:
            return self._item_wrap(data)

    def _item_wrap(self, item):
        return {
            'uuid': item.pop('uuid', None),
            'type': self._type,
            'attributes': item
        }
