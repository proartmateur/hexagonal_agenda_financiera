import typing
import os
from final_class import final
from modules.user.application.create_user import CreateUser

from modules.user.persistence.json_user_repository import JsonUserRepository

current_dir = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(current_dir, "usuarios_db.json")


def crear_usuario(id: str, name: str, password: str):
    user_creator = CreateUser(JsonUserRepository(db))
    user_creator(id, name, password)
