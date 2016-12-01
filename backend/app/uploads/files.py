class UploadedFile:
    def __init__(self, uuid: str, group: str, path: str, link: str):
        self.id = uuid
        self.group = group
        self.path = path
        self.link = link
