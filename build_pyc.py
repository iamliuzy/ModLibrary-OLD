import pathlib
from os.path import abspath
from os import mkdir
import shutil
import toml
import compileall
import re

dist_dir = ".\\dist_pyc\\"
if pathlib.Path(dist_dir).exists():
    shutil.rmtree(dist_dir)

mkdir(dist_dir)

"""
Compile pyc file.
"""
pyc_path_str = "__pycache__\\"
pyc_path = pathlib.Path(pyc_path_str)
if pyc_path.exists():
    shutil.rmtree(pyc_path)
mkdir(pyc_path_str)
compile_excludes = [r"setup\.py", r"build_pyc\.py"]
excludes_regex = ""
index = 0
for exclude in compile_excludes:
    if index == 0:
        excludes_regex = exclude
    else:
        excludes_regex = excludes_regex + "|" + exclude
    index += 1
compileall.compile_dir(".", maxlevels=0, optimize=2, rx=re.compile(excludes_regex))
prog = re.compile(r"(.+)\.cpython-[0-9]+\.opt-2\.pyc")
for f in pyc_path.iterdir():
    m = prog.fullmatch(str(f).replace(abspath(str(pyc_path)), ""))
    if m is not None:
        f.rename(m.group(1) + ".pyc")
for f in pyc_path.iterdir():
    shutil.copy(f, dist_dir + str(f).replace(str(pyc_path_str), ""))


def copy_dir(path: pathlib.Path):
    """
    Copy directory.
    """
    mkdir(dist_dir + str(path).replace(abspath("."), ""))
    for fi in path.iterdir():
        if fi.is_dir():
            copy_dir(fi)
        else:
            shutil.copy(fi, dist_dir + str(file).replace(abspath("."), ""))


"""
Copy resources files.
"""
for file in list(dict(
    dict(dict(dict(toml.loads(open("pyproject.toml", "r", encoding="utf-8").read())).get("tool")).get("distutils")).get(
        "build_exe")).get("include_files")):
    file = str(file)
    file_path = pathlib.Path(file)
    if file_path.is_dir():
        copy_dir(pathlib.Path(file))
    else:
        shutil.copy(file, dist_dir + file.replace(abspath("."), ""))
