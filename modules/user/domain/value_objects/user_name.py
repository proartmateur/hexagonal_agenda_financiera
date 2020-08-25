
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
class UserName(StringValueObject):
    def __init__(self, value):
        super().__init__(value)

