import os
import sys
import tempfile

sys.path.append('..')
from app import app
import unittest

class EventTestCase(unittest.TestCase):

    def set_up(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            app.init_db()

        self.data_post = {
                "color_primary": "#3c2734",
                "color_secondary": "#d5d6d9",
                "description": "New event",
                "end_time": "2016-12-22T12:46:00+00:00",
                "items": [],
                "name": "Event",
                "start_time": "2016-12-22T12:46:00+00:00",
                "target_id": "9dfe9e49-8a5d-4d8f-a3e5-38b7f59e29fe",
                "user_id": "98bb932c-929f-426f-a66c-74b874bf9cd9"
            }

        self.data_put = {
                "color_primary": "#a12c75",
                "color_secondary": "#052804",
                "description": "New event1",
                "end_time": "2016-12-23T08:41:00+00:00",
                "items": [],
                "name": "Event1",
                "start_time": "2016-12-22T08:40:00+00:00",
                "target_id": "9dfe9e49-8a5d-4d8f-a3e5-38b7f59e29fe",
                "user_id": "98bb932c-929f-426f-a66c-74b874bf9cd9"
            }

        self.wrong_data_post = {
                "color_primary": "#3c2734",
                "color_secondary": "#d5d6d9",
                "description": "New event",
                "end_time": "2016-12-22T12:46:00+00:00",
                "items": [],
                "name": 1,
                "start_time": "2016-12-22T12:46:00+00:00",
                "target_id": "9dfe9e49-8a5d-4d8f-a3e5-38b7f59e29fe",
                "user_id": "98bb932c-929f-426f-a66c-74b874bf9cd9"
            }

        self.wrong_data_put = {
                "color_primary": "#a12c75",
                "color_secondary": "#052804",
                "description": "New event1",
                "end_time": "2016-12-23T08:41:00+00:00",
                "items": [],
                "name": 1,
                "start_time": "2016-12-22T08:40:00+00:00",
                "target_id": "9dfe9e49-8a5d-4d8f-a3e5-38b7f59e29fe",
                "user_id": "98bb932c-929f-426f-a66c-74b874bf9cd9"
            }


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_events_list_get(self):
        rv = self.app.get('/events')
        assert rv.status_code == 200

    def test_event_get(self):
        rv = self.app.get('/events/27c6385d-cee1-4eaa-b7c8-c22635f8a418')
        assert rv.status_code == 200

    def test_event_post(self):
        rv = self.app.post('/events', data=self.data_post)
        assert rv.status_code == 200

    def test_event_put(self):
        rv = self.app.put('/events/27c6385d-cee1-4eaa-b7c8-c22635f8a418', data=self.data_put)
        assert rv.status_code == 200

    def test_event_delete(self):
        rv = self.app.delete('/events/27c6385d-cee1-4eaa-b7c8-c22635f8a418')
        assert rv.status_code == 200

    def test_wrong_events_list_get(self):
        rv = self.app.get('/eventss')
        assert rv.status_code == 404

    def test_wrong_event_get(self):
        rv = self.app.get('/events/5')
        assert rv.status_code == 404

    def test_wrong_event_post(self):
        rv = self.app.post('/events', data=self.wrong_data_post)
        assert rv.status_code == 400

    def test_wrong_event_put(self):
        rv = self.app.put('/events/5', data=self.wrong_data_put)
        assert rv.status_code == 400

    def test_wrong_event_delete(self):
        rv = self.app.delete('/events/5')
        assert rv.status_code == 400


if __name__ == '__main__':
    unittest.main()