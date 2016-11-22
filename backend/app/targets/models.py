from sqlalchemy.orm import relationship

from app import db
from app.models import BaseModel


class Target(db.Model, BaseModel):
    __tablename__ = 'targets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    is_done = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('targets.id'))
    user = relationship('User', backref='targets')
    target = relationship('Target', cascade="all, delete-orphan", post_update=True)