from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app import db
from app.models import BaseModel


class Item(BaseModel):
    __tablename__ = 'items'

    event_id = db.Column(UUID, db.ForeignKey('events.id'), nullable=False)
    event = relationship("Event", back_populates="items")
    plugin = db.Column(db.String, nullable=False)
    plugin_item_id = db.Column(db.Integer, nullable=False)
