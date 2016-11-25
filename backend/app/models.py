from random import randint
import uuid as uuid
from sqlalchemy.dialects.postgresql import UUID

from app import db
from app.errors import NotFound


def generate_uuid():
    return uuid.uuid1(randint(1, 281474976710656)).hex


class BaseModel:
    id = db.Column(UUID, primary_key=True, default=generate_uuid)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get(cls, id: str):
        return cls.query.get(id)

    @classmethod
    def get_by(cls, **kw):
        return cls.query.filter_by(**kw).first()

    @classmethod
    def get_or_404(cls, id: str):
        model = cls.get(id)
        if model is None:
            raise NotFound()
        return model

    @classmethod
    def create(cls, **kw):
        model = cls(**kw)
        db.session.add(model)
        return model

    def update(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)

    def save(self):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)

    def __repr__(self):
        values = ', '.join('%s=%r' % (n, getattr(self, n)) for n in self.__table__.c.keys())
        return '%s(%s)' % (self.__class__.__name__, values)
