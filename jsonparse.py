"""
Json file access API.
"""

from os.path import abspath
from pathlib import PurePath
from json import loads, dumps


class JsonFile:
    """
    Json file object
    """

    def __init__(self, path: PurePath, filetype="") -> None:
        """
        :param path: Path of the file.
        :param filetype: Data type of the file, should be "dict" or "list".
        :raise TypeError: If didn't give parameter "filetype" and cannot determine the data type.
        """
        self.path = abspath(path)
        with open(self.path, "r", encoding="utf-8") as file:
            text = file.read()
        if filetype == "":
            if text.startswith("{"):
                filetype = "dict"
            elif text.startswith("["):
                filetype = "list"
            else:
                raise TypeError("Unknown json file type: " + self.path + ".")

        if filetype == "list":
            self.obj = list(loads(text))
        elif filetype == "dict":
            self.obj = dict(loads(text))

    def get(self) -> dict | list:
        """
        :return: All data.
        """
        return self.obj

    def store(self, new: dict | list) -> None:
        """
        Save file and close.
        :param new: New data. It will replace old data.
        """
        with open(self.path, mode="w", encoding="utf-8") as file:
            file.write(dumps(new))


class QuickAccess:
    """
    Provide quick access for a json file.
    """
    @staticmethod
    def json_to_dict(path) -> dict:
        """
        Read json file and return the content.
        """
        return dict(JsonFile(path, "dict").get())

    @staticmethod
    def json_to_list(path) -> list:
        """
        Read json file and return the content.
        """
        return list(JsonFile(path, "list").get())
