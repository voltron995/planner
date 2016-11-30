from marshmallow import Schema
from marshmallow import fields


class UploadSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    group = fields.Str(dump_only=True)
    link = fields.Str(dump_only=True)
