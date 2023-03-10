"""
Json file access API.
"""

#  ModLibrary, a Minecraft mod manager.
#  Copyright (C) 2023 iamliuzy
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see https://www.gnu.org/licenses/.

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


class ManifestAccess:
    @staticmethod
    def manifest_to_dict(path):
        result = {}
        with open(abspath(path), mode="r", encoding="utf-8") as file:
            for line in file.readlines():
                split = line.split(":")
                key = split[0]
                value = split[1].replace(" ", "")
                result[key] = value
        return result
