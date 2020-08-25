import typing
from typing import List
from final_class import final
from modules.user.domain.user import User

from modules.user.domain.user_repository import UserRepository
from shared.persistence.json_repository import JsonRepository


@final
class JsonUserRepository(UserRepository):
    def __init__(self, file_json: str):
        self.__repository = JsonRepository(file_json)

    def save(self, user: User):
        print("Saving: ", user.to_dict())
        self.__repository.save(user.to_dict())

    def find(self, key: str, val: str) -> User:
        data = self.__repository.find(key, val)
        return User(
            data["id"],
            data["name"],
            data["password"],
            data["credits"]
        )

    def list(self) -> List[User]:
        users_list = []
        for data in self.__repository.list():
            users_list.append(
                User(
                    data["id"],
                    data["name"],
                    data["password"],
                    data["credits"]
                )
            )

        return users_list
