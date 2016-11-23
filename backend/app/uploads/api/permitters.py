from app.api import Permitter
from app.errors import Forbidden, AccessDenied
from app.uploads.uploads_manager import UploadsManager


class UploadPermitter(Permitter):
    def post(self):
        pass


class DownloadPermitter(Permitter):
    def get(self):
        args = self._request.view_args
        # Check if current user is the owner of the file.
        if not UploadsManager.is_file(args.get('file_uuid'), args.get('group')):
            raise Forbidden(AccessDenied('You are not allowed to this file'))
