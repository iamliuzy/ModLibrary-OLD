"""
Json file access API.
"""

import os.path
from pathlib import PurePath
import json



class JsonFile:
    """
    Json file object
    """
    def __init__(self, path: PurePath, filetype="") -> None:
        """
        :param filetype: Data type of the file, should be "dict" or "list".
        """
        self.path = os.path.abspath(path)
        with open(self.path, "r", encoding="utf-8") as file:
            self.text = file.read()
        if filetype == "":
            if self.text.startswith("{"):
                filetype = "dict"
            elif self.text.startswith("["):
                filetype = list
            else:
                raise TypeError("Unkdown json file type: " + self.path + ".")

        if filetype == "list":
            self.obj = list(json.loads(self.text))
        elif filetype == "dict":
            self.obj = dict(json.loads(self.text))

    def edit(self, new: list | dict) -> None:
        """
        Edit the json file.
        :param new: Datas to write in. It will **replace** the old datas.
        """
        self.obj = new
        self.text = str(new)

    def get(self) -> dict | list:
        """
        Return all the datas.
        """
        return self.obj

    def store(self) -> None:
        """
        Save file and close.
        """
        with open(self.path, mode="w", encoding="utf-8") as file:
            file.write(self.text)


class QuickAccess:
    """
    Provide quick access for a json file.
    """
    @staticmethod
    def json_to_dict(path) -> dict:
        """
        Read json file and return the content.
        """
        file = JsonFile(path, "dict")
        content = file.get()
        file.store()
        return content

    @staticmethod
    def json_to_list(path) -> list:
        """
        Read json file and return the content.
        """
        file = JsonFile(path, "list")
        content = file.get()
        file.store()
        return content
