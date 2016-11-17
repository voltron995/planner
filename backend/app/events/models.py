from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app import db
from app.models import BaseModel


class Event(db.Model, BaseModel):
    __tablename__ = 'events'

    name = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship('User', backref='events')
    # target_id = db.Column(db.Integer, db.ForeignKey('targets.id'))
    # target = relationship('Target', backref='event')
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    status = db.Column(db.Boolean)
