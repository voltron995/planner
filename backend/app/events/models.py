from ..database import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..msclient.models import *
from ..users.models import *

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship('User', backref='events')
    target_id = db.Column(db.Integer, db.ForeignKey('targets.id'))
    target = relationship('Target', backref='event')
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    status = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    updatet_at = db.Column(db.DateTime)

class Target(db.Model):
    __tablename__ = 'targets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship('User', backref='profiles')
    target_id = db.Column(db.Integer, db.ForeignKey('targets.id'))
    target = relationship('Target', backref='targets')
    status = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    updatet_at = db.Column(db.DateTime)

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    user = relationship('Event', backref='items')
    # plugin_item_id - ?
    plugin_id = db.Column(db.Integer, db.ForeignKey('plugins.id'))
    user = relationship('Plugin', backref='items')
    created_at = db.Column(db.DateTime)
    updatet_at = db.Column(db.DateTime)
