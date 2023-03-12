import toml, shutil
from os.path import abspath

for file in list(dict(dict(toml.loads(open("pyproject.toml", "r", encoding="utf-8").read())).get("tool.distutils.build_exe")).get("include_files")):
    shutil.copy(abspath(file), abspath(".\\dist\\"))