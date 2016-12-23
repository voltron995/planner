import sys
sys.path.append('..')
from app import app
import os
import unittest
import tempfile

class TargetTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            app.init_db()

        self.data_post = {
            "created_at": "2016-12-21T11:49:19.469833+00:00",
            "description": "To be healthy, i should stay fit.",
            "id": "abddba3a-0c18-48f1-a9f6-b57f15d388b0",
            "is_done": False,
            "name": "be healthy",
            "target_id": "cc5aff55-c4ab-4558-9915-070d051a27a5",
            "updated_at": "2016-12-21T11:49:19.469833+00:00",
            "user_id": "985212c0-b6f9-4422-8741-95dc8e06ec0e"
        }
        self.data_put = {

            "created_at": "2016-12-21T11:49:19.469833+00:00",
            "description": "Not To be healthy, i should stay fit.",
            "id": "abddba3a-0c18-48f1-a9f6-b57f15d388b0",
            "is_done": True,
            "name": "not be healthy",
            "target_id": "cc5aff55-c4ab-4558-9915-070d051a27a5",
            "updated_at": "2016-12-21T11:49:19.469833+00:00",
            "user_id": "985212c0-b6f9-4422-8741-95dc8e06ec0e"
        }

        self.wrong_data_post = {
            "created_at": "2016-12-21T11:49:19.469833+00:00",
            "description": "To be healthy, i should stay fit.",
            "id": "abddba3a-0c18-48f1-a9f6-b57f15d388b0",
            "is_done": False,
            "name": 1,
            "target_id": "cc5aff55-c4ab-4558-9915-070d051a27a5",
            "updated_at": "2016-12-21T11:49:19.469833+00:00",
            "user_id": "985212c0-b6f9-4422-8741-95dc8e06ec0e"
        }

        self.wrong_data_put = {
            "created_at": "2016-12-21T11:49:19.469833+00:00",
            "description": "Not To be healthy, i should stay fit.",
            "id": "abddba3a-0c18-48f1-a9f6-b57f15d388b0",
            "is_done": True,
            "name": "not be healthy",
            "target_id": "cc5aff55-c4ab-4558-9915-070d051a27a5",
            "updated_at": "2016-12-21T11:49:19.469833+00:00",
            "user_id": "985212c0-b6f9-4422-8741-95dc8e06ec0e"
        }


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_target_post(self):
        rv = self.app.post('/targets', data=self.data_post)
        assert rv.status_code == 200

    def test_target_put(self):
        rv = self.app.put('/targets/cc5aff55-c4ab-4558-9915-070d051a27a5', data=self.data_put)
        assert rv.status_code == 200

    def test_targets_list_get(self):
        rv = self.app.get('/targets')
        assert rv.status_code == 200

    def test_target_get(self):
        rv = self.app.get('/targets/cc5aff55-c4ab-4558-9915-070d051a27a5')
        assert rv.status_code == 200

    def test_target_delete(self):
        rv = self.app.delete('/targets/cc5aff55-c4ab-4558-9915-070d051a27a5')
        assert rv.status_code == 200

    def test_wrong_targets_list_get(self):
        rv = self.app.get('/targetsss')
        assert rv.status_code == 404

    def test_wrong_target_get(self):
        rv = self.app.get('/targets/5')
        assert rv.status_code == 404

    def test_wrong_target_post(self):
        rv = self.app.post('/targets', data=self.wrong_data_post)
        assert rv.status_code == 400

    def test_wrong_target_put(self):
        rv = self.app.put('/targets/5', data=self.wrong_data_put)
        assert rv.status_code == 400

    def test_wrong_target_delete(self):
        rv = self.app.delete('/targets/5')
        assert rv.status_code == 400

if __name__ == '__main__':
    unittest.main()