
"""

    Value Object

    Project: Mi proyecto 1.0
    Version: 1.0
    Author: Enrique Nieto Martínez

"""
    
import typing
from final_class import final
from shared.domain.value_objects.string_value_object import StringValueObject


@final
class UserPassword(StringValueObject):
    def __init__(self, value):
        if len(value) < 6:
            raise Exception("Un password debe ser mayor a 6 caracteres")
        super().__init__(value)

