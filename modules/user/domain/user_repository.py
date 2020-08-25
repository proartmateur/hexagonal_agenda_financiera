import typing

from abc import ABCMeta, abstractmethod
from modules.user.domain.user import User


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User):
        pass

    @abstractmethod
    def find(self, key: str, val: str):
        pass

    @abstractmethod
    def list(self):
        pass
