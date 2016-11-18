import enum

from sqlalchemy.orm import relationship

from app import db
from app.models import BaseModel


class Status(enum.Enum):
    achieved = 'achieved'
    in_progress = 'in_progress'
    failed = 'failed'


class Target(db.Model, BaseModel):
    __tablename__ = 'targets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum(Status))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('targets.id'))
    user = relationship('User', backref='targets')
