from flask import url_for
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from passlib.handlers.sha2_crypt import sha256_crypt

from app import db
from app.models import BaseModel
from app.uploads import groups
from app.uploads.manager import UploadsManager


class User(BaseModel, UserMixin):
    __tablename__ = 'users'

    login = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    last_access = db.Column(db.DateTime)

    profile = relationship('Profile', uselist=False, backref='user')

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = sha256_crypt.encrypt(password)

    def verify_password(self, password: str):
        return sha256_crypt.verify(password, self.password_hash)

    def get_id(self):
        return self.id


class Profile(BaseModel):
    __tablename__ = 'profiles'

    user_id = db.Column(UUID, db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    birth_date = db.Column(db.Date)
    image = db.Column(db.String(64))

    @property
    def image_link(self):
        # todo: is this ugly or not?
        if self.image:
            return UploadsManager.get_link(self.image, groups.PROFILE_IMAGES)
        else:
            return url_for('static', filename='assets/avatar-default.png')
