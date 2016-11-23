from app.api import Api

api_uploads = Api('uploads', url_prefix='/uploads')

from . import urls
