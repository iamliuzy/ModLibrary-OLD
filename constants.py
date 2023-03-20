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
import toml

LICENSE_TEXT = """
               ModLibrary, a Minecraft mod manager.
               Copyright (C) 2022  iamliuzy

               This program is free software: you can redistribute it and/or modify
               it under the terms of the GNU General Public License as published by
               the Free Software Foundation, either version 3 of the License, or
                any later version.

               This program is distributed in the hope that it will be useful,
               but WITHOUT ANY WARRANTY; without even the implied warranty of
               MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
               GNU General Public License for more details.

               You should have received a copy of the GNU General Public License
               along with this program.  If not, see https://www.gnu.org/licenses/.

               E-mail: liuzhiyu.sh@outlook.com
               """

_toml = toml.load(open(abspath(".\\pyproject.toml"), encoding="utf-8"))
_project = _toml.get("project")
NAME = _project.get("name")
VERSION = _project.get("version")
DESCRIPTION = _project.get("description")


class Namespace(object):
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        return self.__dict__.get(item)
