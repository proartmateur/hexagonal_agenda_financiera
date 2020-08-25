from unittest import TestCase
from modules.user.domain.user import User
from modules.user.domain.value_objects.user_uid import UserUid
from modules.user.domain.value_objects.user_name import UserName
from modules.user.domain.value_objects.user_password import UserPassword
from modules.user.domain.value_objects.user_credits import UserCredits


class TestUser(TestCase):
    def test_create_new_user(self):
        pablo = User(UserUid("01202"), UserName("Pablo López"), UserPassword("12345678"))
        self.assertEqual(pablo.credits.value, 100)

    def test_load_existent_user(self):
        user_from_data = {
            "uid": "01202",
            "name": "Julia",
            "pass": "123456",
            "credits": 320
        }
        pablo = User(
            UserUid(user_from_data["uid"]),
            UserName(user_from_data["name"]),
            UserPassword(user_from_data["pass"]),
            UserCredits(user_from_data["credits"])
        )
        self.assertEqual(pablo.credits.value, 320)

    def test_deposit(self):
        # creamos un nuevo usuario
        pablo = User(UserUid("01202"), UserName("Pablo López"), UserPassword("12345678"))

        # realizamos un depósito
        pablo.deposit(100)
        self.assertEqual(pablo.credits.value, 200)

    def test_charge(self):
        # creamos un nuevo usuario
        pablo = User(UserUid("01202"), UserName("Pablo López"), UserPassword("12345678"))

        # realizamos un cargo
        pablo.charge(10)
        self.assertEqual(pablo.credits.value, 90)

    def test_sould_be_dead(self):
        # cargamos un usuario con 10 créditos
        pablo = User(UserUid("01202"), UserName("Pablo López"), UserPassword("12345678"), UserCredits(10))

        # realizamos un cargo
        pablo.charge(10)

        # tenía 10 y se le cargó 10 entonces queda como inactivo
        self.assertFalse(pablo.active)

    def test_sould_be_vip(self):
        # creamos un nuevo usuario
        pablo = User(UserUid("01202"), UserName("Pablo López"), UserPassword("12345678"))

        # realizamos un cargo
        pablo.deposit(1_000_000)

        print(pablo.is_vip)
        self.assertTrue(pablo.is_vip)