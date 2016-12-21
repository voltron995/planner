from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app import db
from app.models import BaseModel


class Target(BaseModel):
    __tablename__ = 'targets'

    name = db.Column(db.String(255), nullable=False)
    is_done = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(UUID, db.ForeignKey('users.id'), nullable=False)
    target_id = db.Column(UUID, db.ForeignKey('targets.id'))
    description = db.Column(db.String)
    user = relationship('User', backref='targets')
    target = relationship('Target', cascade='all, delete-orphan', post_update=True)
    events = relationship("Event", back_populates='target',
                    cascade="all, delete, delete-orphan")