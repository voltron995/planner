import os
from datetime import datetime, timedelta
from shutil import copyfile
from uuid import uuid4

from app import app
from app.uploads import groups
from app.uploads.files import UploadedFile


class UploadsManager:
    @classmethod
    def get_tmp_file(cls, uuid: str) -> UploadedFile:
        return cls.get_file(uuid, group=groups.TEMPORARY_FILES)

    @classmethod
    def save_tmp_file(cls, file):
        return cls.save_file(file, group=groups.TEMPORARY_FILES)

    @classmethod
    def is_tmp_file(cls, uuid: str):
        return cls.is_file(uuid, groups.TEMPORARY_FILES)

    @classmethod
    def remove_tmp_files(cls):
        return cls.remove_files(groups.TEMPORARY_FILES)

    @classmethod
    def get_file(cls, uuid: str, group: str) -> UploadedFile:
        path = cls.get_path(uuid, group)
        if not os.path.isfile(path):
            raise FileNotFoundError
        link = cls.get_link(uuid, group)
        return UploadedFile(uuid=uuid, group=group, path=path, link=link)

    @classmethod
    def save_file(cls, file, group: str) -> UploadedFile:
        uuid = cls.unique_identifier(file)
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
        os.rename(file.path, cls.get_path(file.id, to_group))
        return cls.get_file(uuid=file.id, group=to_group)

    @classmethod
    def copy_file(cls, file: UploadedFile, to_group: str) -> UploadedFile:
        folder = cls.get_folder(to_group)
        if not os.path.exists(folder):
            os.makedirs(folder)
        copyfile(file.path, cls.get_path(file.id, to_group))
        return cls.get_file(uuid=file.id, group=to_group)

    @classmethod
    def is_file(cls, uuid: str, group: str) -> bool:
        return os.path.isfile(cls.get_path(uuid, group))

    @classmethod
    def get_path(cls, uuid: str, group: str) -> str:
        return os.path.join(cls.get_folder(group), uuid)

    @classmethod
    def get_folder(cls, group: str) -> str:
        return os.path.join(app.config.get('UPLOAD_FOLDER'), group)

    @classmethod
    def unique_identifier(cls, file) -> str:
        return uuid4().hex + '.' + file.filename.split('.').pop()

    @classmethod
    def get_link(cls, uuid: str, group: str) -> str:
        return os.path.join(app.config.get('UPLOADED_FILES_URL'), group, uuid)

    @classmethod
    def remove_files(cls, group: str, older_than: timedelta = timedelta(hours=24)):
        files_removed = 0
        current_time = datetime.now()
        for f in os.listdir(cls.get_folder(group)):
            f_path = cls.get_path(f, group)
            creation_time = datetime.fromtimestamp(os.path.getmtime(f_path))
            if (current_time - creation_time) >= older_than:
                os.remove(f_path)
                files_removed += 1
        print('{num} files were removed from the "{group}" upload directory.'.format(num=files_removed, group=group))
