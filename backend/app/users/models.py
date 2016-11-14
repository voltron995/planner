from flask_login import UserMixin
from sqlalchemy.orm import relationship
from passlib.handlers.sha2_crypt import sha256_crypt

from app import db
from app.models import BaseModel


class User(db.Model, BaseModel, UserMixin):
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
        return self.uuid


class Profile(db.Model, BaseModel):
    __tablename__ = 'profiles'

    #todo: uuid
    uuid = 'fkfsdkjvlnervjnerkvjnevjkn'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    birth_date = db.Column(db.Date)
    image_path = db.Column(db.String(255))
