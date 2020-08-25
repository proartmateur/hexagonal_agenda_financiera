class IntValueObject(object):
    def __init__(self, value: int):
        if not (isinstance(value, type(12))):
            raise Exception('ValueObject', f'IntValueObject: Se esperaba int pero se obtuvo {type(value)}')

        self.__value = value

    @property
    def value(self):
        return self.__value