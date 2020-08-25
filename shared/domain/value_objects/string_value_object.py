class StringValueObject(object):
    def __init__(self, value: str):
        if not (isinstance(value, type("str"))):
            raise Exception('ValueObject', f'StringValueObject: Se esperaba str pero se obtuvo {type(value)}')

        self.__value = value

    @property
    def value(self):
        return self.__value