from random import randint
import uuid as uuid
from app import db


def generate_uuid():
    return uuid.uuid1(randint(1, 281474976710656)).hex

class BaseModel:
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(64), unique=True, nullable=False, default=generate_uuid)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
