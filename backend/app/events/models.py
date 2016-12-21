from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app import db
from app.models import BaseModel


class Event(BaseModel):
    __tablename__ = 'events'

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    user_id = db.Column(UUID, db.ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='events')
    target_id = db.Column(UUID, db.ForeignKey('targets.id'))
    target = relationship('Target', cascade='all, delete-orphan', backref='event')
    start_time = db.Column(db.DateTime(timezone=True), nullable=False)
    end_time = db.Column(db.DateTime(timezone=True), nullable=False)
    color_primary = db.Column(db.String(), default='#aaa')
    color_secondary = db.Column(db.String(), default='#bbb')
    is_done = db.Column(db.Boolean, nullable=False, default=False)
