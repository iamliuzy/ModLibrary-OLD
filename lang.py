import locale
import os.path

import jsonparse


locale = locale.getdefaultlocale()[0].lower()
lang_path = os.path.abspath(".\\lang")
file_path = os.path.join(lang_path, locale)
en_file_path = os.path.join(lang_path, "en_us.json")

if not os.path.exists(file_path):
    file_path = en_file_path

lang_dict = dict(jsonparse.QuickAccess.json_to_dict(file_path))
en_lang_dict = dict(jsonparse.QuickAccess.json_to_dict(en_file_path))


def _(s):
    result: str = lang_dict.get(s)
    if result is None:
        result = en_lang_dict.get(s)
        if result is None:
            result = s
    return result
