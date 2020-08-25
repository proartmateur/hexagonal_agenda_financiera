import typing
from final_class import final

# region Conectando con la capa Domain
from modules.user.domain.user import User
from modules.user.domain.value_objects.user_uid import UserUid
from modules.user.domain.value_objects.user_name import UserName
from modules.user.domain.value_objects.user_password import UserPassword
from modules.user.domain.value_objects.user_credits import UserCredits

# -- Contrato para la persistencia de datos
from modules.user.domain.user_repository import UserRepository


# endregion

@final
class CreateUser:
    def __init__(self, repository: UserRepository):
        # Inyectamos cualquier repositorio que cumpla el contrato
        # DIP: Cumplimos con Dependency Inversion Principle
        self.__repository = repository

    def __call__(self, uid: str, name: str, password: str):
        uid = UserUid(uid)
        name = UserName(name)
        password = UserPassword(password)

        # Creamos el usuario en memoria
        user = User(uid, name, password)

        # persistimos el usuario
        self.__repository.save(user)

        # Ejecutamos tareas correspondientes al evento de dominio
