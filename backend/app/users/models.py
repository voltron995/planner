from app import db
from sqlalchemy.orm import relationship

from app import login_manager


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # # login = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    # # last_access = db.Column(db.DateTime)
    # # is_active = db.Column(db.Boolean)
    # # created_at = db.Column(db.D   ateTime)
    # # updated_at = db.Column(db.DateTime)
    #
    is_active = True #todo:
    is_authenticated = False
    is_anonymous = False

    def get_id(self):
        return self.id


# class Profile(db.Model):
#     __tablename__ = 'profiles'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = relationship('User', backref='profiles')
#     first_name = db.Column(db.String)
#     last_name = db.Column(db.String)
#     birth_date = db.Column(db.String)
#     image_path = db.Column(db.String)
#     created_at = db.Column(db.DateTime)
#     updated_at = db.Column(db.DateTime)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
