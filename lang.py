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

import _locale
import os.path
import jsonparse


local = _locale._getdefaultlocale()[0].lower() + ".json"
lang_path = os.path.abspath(".\\lang")
file_path = os.path.join(lang_path, local)
en_file_path = os.path.join(lang_path, "en_us.json")

if not os.path.exists(file_path):
    file_path = en_file_path

lang_dict = dict(jsonparse.QuickAccess.json_to_dict(file_path))
en_lang_dict = dict(jsonparse.QuickAccess.json_to_dict(en_file_path))


def trans(string):
    result: str = lang_dict.get(string)
    if result is None:
        result = en_lang_dict.get(string)
        if result is None:
            result = string
    return result
