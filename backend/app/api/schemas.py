from marshmallow import Schema, fields


class ModelSchema(Schema):
    id = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ErrorSchema(Schema):
    title = fields.Str(dump_only=True)
    detail = fields.Str(dump_only=True)
    status = fields.Int(dump_only=True)
    source = fields.Str(dump_only=True)
