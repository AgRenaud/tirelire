from unittest import TestCase
from typing import List

from app.domain import commands, model



class TestUser(TestCase):

    def test_create_user_and_add_app_auth(self):
        new_user = model.User('123', 'password', 'john', 'doe', 'jdoe@mail.com')
        new_user.add_app_auth(model.AppAuthorization(model.App.TIRELIRE_APP))
        self.assertEqual(new_user._applications_auth, {model.AppAuthorization(model.App.TIRELIRE_APP)})

        with self.assertRaises(ValueError):
            new_user.add_app_auth(model.AppAuthorization(model.App.TIRELIRE_APP))