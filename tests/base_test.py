import os

from flask_testing import TestCase

from localizeapp import app, db
from localizeapp.auth.models import User


class BaseTestCase(TestCase):
    TESTING = True

    def create_app(self):
        app.config.from_object("config.TestingConfig")
        return app

    def setUp(self):
        with self.app.app_context():
            db.create_all()
        user = User(email="ad@min.com", password="admin_user")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        # testdb_path = os.path.join("instance", "testdb.sqlite")
        # os.remove(testdb_path)
