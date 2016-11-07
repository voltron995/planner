from flask import current_app
from flask_login import UserMixin
from itsdangerous import Serializer
from sqlalchemy.orm import relationship

from app import db
from app.mixins import TimestampsMixin
from .helpers import verify_password, encrypt_password


class User(UserMixin, TimestampsMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
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
        self.password_hash = encrypt_password(password)

    def verify_password(self, password: str):
        return verify_password(password, self.password_hash)

    def get_id(self):
        return self.id

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.is_active = True
        db.session.add(self)
        return True


class Profile(TimestampsMixin, db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    birth_date = db.Column(db.Date)
    image_path = db.Column(db.String(255))
