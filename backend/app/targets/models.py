from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app import db
from app.models import BaseModel


class Target(BaseModel):
    __tablename__ = 'targets'

    name = db.Column(db.String(255), nullable=False)
    # todo: default false and nullable false
    is_done = db.Column(db.Boolean)
    user_id = db.Column(UUID, db.ForeignKey('users.id'), nullable=False)
    target_id = db.Column(UUID, db.ForeignKey('targets.id'))
    user = relationship('User', backref='targets')
    target = relationship('Target', cascade='all, delete-orphan', post_update=True)
