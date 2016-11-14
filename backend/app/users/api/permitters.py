from app.api import Permitter


class UserSingle(Permitter):
    def get(self):
        print('one user - permitted')