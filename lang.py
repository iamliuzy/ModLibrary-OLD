"""
Provide I18N Interface.
"""
import locale
import os.path
import jsonparse


locale.setlocale(locale.LC_ALL, '')
local = locale.getlocale()[0].lower() + ".json"
lang_path = os.path.abspath(".\\lang")
file_path = os.path.join(lang_path, local)
en_file_path = os.path.join(lang_path, "en_us.json")

if not os.path.exists(file_path):
    file_path = en_file_path

lang_dict = dict(jsonparse.QuickAccess.json_to_dict(file_path))
en_lang_dict = dict(jsonparse.QuickAccess.json_to_dict(en_file_path))


def _(string):
    result: str = lang_dict.get(string)
    if result is None:
        result = en_lang_dict.get(string)
        if result is None:
            result = string
    return result
