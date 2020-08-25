from unittest import TestCase

from modules.user.domain.user import User
from modules.user.domain.value_objects.user_uid import UserUid
from modules.user.domain.value_objects.user_name import UserName
from modules.user.domain.value_objects.user_password import UserPassword
from modules.user.domain.value_objects.user_credits import UserCredits

from modules.user.persistence.json_user_repository import JsonUserRepository


class TestUser(TestCase):
    def test_if_persist_user(self):
        pablo = User(UserUid("01202"), UserName("Pablo López"), UserPassword("12345678"))

        self.assertEqual(pablo.credits.value, 100)
