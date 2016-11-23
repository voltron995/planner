from app.api import Permitter


class UserCurrent(Permitter):
    def put(self):
        # todo: do we have something to permit?
        pass


class ProfileCurrent(Permitter):
    def put(self):
        # todo: do we have something to permit?
        pass
