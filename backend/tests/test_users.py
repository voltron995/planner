import os
import tempfile

from flask import Flask
from app import app
import sys
import unittest
sys.path.append('..')

class UserTestCase(unittest.TestCase):

    def set_up(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            app.init_db()

        self.user_login_data = {
                "email": "planner123@mailinator.com",
                "password": "123456"
            }

        self.user_register_data = {
                "email": "planner123456@mailinator.com",
                "password": "123456",
                "confirm": "123456",
                "login": "one"
            }

        self.user_resend_confirmation_data = {
                "email": "planner123@mailinator.com"
            }

        self.wrong_user_login_data = {
                "email": "planner123",
                "password": "123456"
            }

        self.wrong_user_register_data = {
                "email": "planner",
                "password": "123456",
                "confirm": "123456",
                "login": "one"
            }

        self.wrong_user_resend_confirmation_data = {
                "email": "planner12345698798@mailinator.com"
            }

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_target_get(self):
        rv = self.app.get('/users/current')
        assert rv.status_code == 200

    def test_user_login_post(self):
        rv = self.app.post('/users/login', data=self.user_login_data)
        assert rv.status_code == 200

    def test_user_register_post(self):
        rv = self.app.post('/users/register', data=self.user_register_data)
        assert rv.status_code == 200

    def test_user_resend_confirmation_post(self):
        rv = self.app.post('/users/resend', data=self.user_resend_confirmation_data)
        assert rv.status_code == 200

    def test_wrong_user_login_post(self):
        rv = self.app.post('/users/login', data=self.user_login_data)
        assert rv.status_code == 302

    def test_wrong_user_register_post(self):
        rv = self.app.post('/users/register', data=self.user_register_data)
        assert rv.status_code == 302

    def test_wrong_user_resend_confirmation_post(self):
        rv = self.app.post('/users/resend', data=self.user_resend_confirmation_data)
        assert rv.status_code == 302


if __name__ == '__main__':
    unittest.main()