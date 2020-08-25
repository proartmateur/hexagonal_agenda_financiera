import typing
from final_class import final

# Persistencia
import json
import os


@final
class JsonRepository(object):

    def __init__(self, file_json):
        self.__file_json = file_json
        self.__data = []

        if not os.path.exists(file_json):
            self.__write_file("[]")

    def __write_file(self, content: str):
        with open(self.__file_json, "w", encoding="utf-8") as file:
            file.write(content)

    # command
    def save(self, item: dict):
        """Add new row to db"""
        data = self.list()
        data.append(item)
        # Persistir en storage
        self.__write_file(json.dumps(data))

    # Query
    def find(self, key: str, id: str) -> dict:
        data = self.list()
        for item in data:
            if item[key] == id:
                return item

    # Query
    def list(self) -> list:
        print(f"reading: {self.__file_json}")
        with open(self.__file_json, "r", encoding="utf-8") as file:
            data = file.read()

            print("Data:", data)
        return json.loads(data)
