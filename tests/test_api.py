import unittest

from flask_bcolz.app import create_app


class FlaskBcolzTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        self.app = app.test_client()

    def test_a(self):
        r = self.app.get('/status')
        assert r.status_code == 200


if __name__ == '__main__':
    unittest.main()
