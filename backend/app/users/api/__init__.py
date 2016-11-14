from app.api import Api

api_users = Api('users', url_prefix='/users')
api_profiles = Api('profiles', url_prefix='/profiles')

from . import urls
