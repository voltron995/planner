from sqlalchemy.orm import relationship

from app import db
from .helpers import verify_password


# todo: move out to mixins file.
class Timestamps:
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())


class User(Timestamps, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    last_access = db.Column(db.DateTime)

    profile = relationship('Profile', uselist=False, backref='user')

    is_authenticated = True
    is_anonymous = False

    def get_id(self):
        return self.id

    def verify_password(self, password: str):
        return verify_password(password, self.password)


class Profile(Timestamps, db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    birth_date = db.Column(db.Date)
    image_path = db.Column(db.String(255))
