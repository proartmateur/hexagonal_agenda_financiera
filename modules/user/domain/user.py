"""

    Domain Class User

    Project: Mi proyecto 1.0
    Version: 1.0
    Author: Enrique Nieto Martínez

"""

import typing
from final_class import final

from modules.user.domain.value_objects.user_uid import UserUid
from modules.user.domain.value_objects.user_name import UserName
from modules.user.domain.value_objects.user_password import UserPassword
from modules.user.domain.value_objects.user_credits import UserCredits


@final
class User(object):
    # region Internal
    def __init__(self, uid: UserUid, name: UserName, password: UserPassword, credits: UserCredits = UserCredits(100)):
        #region Estado
        self.__uid = uid
        self.__name = name
        self.__password = password
        self.__credits = credits

        self.__is_vip = False
        self.__is_dead = False
        self.__VIP_MIN_CREDITS = 1_000_000
        #endregion

    def __str__(self):
        return f'- User: uid: {self.__uid.value}, name: {self.__name.value}, password: {self.__password.value} , credits: {self.__credits.value}'

    def __repr__(self):
        return f'- User: uid: {self.__uid.value}, name: {self.__name.value}, password: {self.__password.value} , credits: {self.__credits.value}'

    def to_dict(self):
        return {
            "id": self.__uid.value,
            "name": self.__name.value,
            "password": self.__password.value,
            "credits": self.__credits.value
        }

    def __update_credits(self, val: int):
        val = UserCredits(val)
        self.__credits = val

        val = val.value
        if val >= self.__VIP_MIN_CREDITS:
            self.__is_vip = True

        if val < self.__VIP_MIN_CREDITS:
            self.__is_vip = False
        if val < 1:
            self.__is_dead = True


    # endregion

    # region Getters

    @property
    def active(self):
        return not self.__is_dead

    @property
    def credits(self):
        return self.__credits

    @property
    def uid(self) -> UserUid:
        return self.__uid

    @property
    def name(self) -> UserName:
        return self.__name

    @property
    def password(self) -> UserPassword:
        return self.__password

    @property
    def is_vip(self):
        return self.__is_vip

    # endregion

    # region Behavior

    def deposit(self, val: int):
        new_val = UserCredits(val).value
        current = self.__credits.value
        self.__update_credits(current + new_val)

    def charge(self, val: int):
        if self.__is_vip:
            val = val - 1
        charge_val = UserCredits(val).value
        current = self.__credits.value
        self.__update_credits(current - charge_val)

    # endregion
