import os
from datetime import datetime, timedelta
from uuid import uuid4

from flask import url_for
from flask_login import current_user

from app import app


class UploadedFile:
    def __init__(self, uuid: str, group: str, path: str, link: str):
        self.uuid = uuid
        self.group = group
        self.path = path
        self.link = link


# todo: do we need class where all methods are class methods?
class UploadsManager:
    TMP_GROUP = 'tmp'

    @classmethod
    def get_tmp_file(cls, uuid: str) -> UploadedFile:
        return cls.get_file(uuid, group=cls.TMP_GROUP)

    @classmethod
    def save_tmp_file(cls, file):
        return cls.save_file(file, group=cls.TMP_GROUP)

    @classmethod
    def is_tmp_file(cls, uuid: str):
        return cls.is_file(uuid, cls.TMP_GROUP)

    @classmethod
    def remove_tmp_files(cls):
        return cls.remove_files(cls.TMP_GROUP)

    @classmethod
    def get_file(cls, uuid: str, group: str) -> UploadedFile:
        path = cls.get_path(uuid, group)
        if not os.path.isfile(path):
            raise FileNotFoundError
        link = cls.get_link(uuid, group)
        return UploadedFile(uuid=uuid, group=group, path=path, link=link)

    @classmethod
    def save_file(cls, file, group: str) -> UploadedFile:
        uuid = cls.unique_identifier()
        folder = cls.get_folder(group)
        if not os.path.exists(folder):
            os.makedirs(folder)
        file.save(os.path.join(folder, uuid))
        return cls.get_file(uuid=uuid, group=group)

    @classmethod
    def move_file(cls, file: UploadedFile, to_group: str) -> UploadedFile:
        folder = cls.get_folder(to_group)
        if not os.path.exists(folder):
            os.makedirs(folder)
        os.rename(file.path, cls.get_path(file.uuid, to_group))
        return cls.get_file(uuid=file.uuid, group=to_group)

    @classmethod
    def is_file(cls, uuid: str, group: str) -> bool:
        return os.path.isfile(cls.get_path(uuid, group))

    @classmethod
    def get_path(cls, uuid: str, group: str) -> str:
        return os.path.join(cls.get_folder(group), uuid)

    @classmethod
    def get_folder(cls, group: str, user=current_user) -> str:
        path = os.path.join(app.config['UPLOAD_FOLDER'], group)
        if user:
            path = os.path.join(path, user.uuid)
        return path

    @classmethod
    def unique_identifier(cls) -> str:
        return uuid4().hex

    @classmethod
    def get_link(cls, uuid: str, group: str) -> str:
        return url_for('api.uploads.download', group=group, file_uuid=uuid)

    @classmethod
    def remove_files(cls, group: str, older_than: timedelta = timedelta(hours=24)):
        raise NotImplementedError
        files_removed = 0
        current_time = datetime.now()
        for f in os.listdir(cls.get_folder(group, user=None)):
            # todo: "f" is user folder, not a file yet. Files are inside user folder.
            f_path = cls.get_path(f, group)
            creation_time = datetime.fromtimestamp(os.path.getmtime(f_path))
            if (current_time - creation_time) >= older_than:
                os.remove(f_path)
                files_removed += 1
        print('{num} files were removed from the "{group}" upload directory.'.format(num=files_removed, group=group))
