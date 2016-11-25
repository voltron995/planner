from random import randint
import uuid as uuid
from sqlalchemy.dialects.postgresql import UUID

from app import db


def generate_uuid():
    return uuid.uuid1(randint(1, 281474976710656)).hex


class BaseModel:
    id = db.Column(UUID, primary_key=True, default=generate_uuid)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
