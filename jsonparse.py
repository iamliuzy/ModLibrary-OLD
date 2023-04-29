#  ModLibrary, a Minecraft mod manager.
#  Copyright (C) 2023 iamliuzy
#
#  This file is part of ModLibrary.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#   any later version.
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
    Provide access for a JSON file.
    """

    def __init__(self, path: PurePath, filetype: str = "") -> None:
        """
        Create a new JsonFile instance.

        :param path: Path to the JSON file.
        :param filetype: Type of the JSON file.
        :raises TypeError: If the filetype is not specified and cannot be determined.
        :raises json.JSONDecodeError: If the JSON file contains invalid data.
        """
        self.path = abspath(path)
        with open(self.path, "r", encoding="utf-8") as file:
            text = file.read()
        if filetype == "":
            try:
                self.obj = loads(text)
            except ValueError:
                raise TypeError(f"Cannot determine the JSON file type: {self.path}")
        elif filetype == "list":
            self.obj = list(loads(text))
        elif filetype == "dict":
            self.obj = dict(loads(text))
        else:
            raise ValueError(f"Unknown JSON file type: {filetype}")

    def get(self) -> dict | list:
        """
        Get the JSON data.

        :return: The JSON data.
        """
        return self.obj

    def store(self, new: dict | list) -> None:
        """
        Store the JSON data.

        :param new: The new JSON data.
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
    """
    Provide access for a manifest file.
    """

    @staticmethod
    def manifest_to_dict(path):
        result = {}
        with open(abspath(path), mode="r", encoding="utf-8") as file:
            for line in map(str.strip, file.readlines()):
                if not (":" in line):
                    continue
                key, value = line.split(":", maxsplit=1)
                result[key] = value.strip()
        return result
