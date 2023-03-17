import pathlib
from os.path import abspath
from os import mkdir
import shutil
import toml
import compileall
import re

distdir = ".\\dist_pyc\\"
if pathlib.Path(distdir).exists():
    shutil.rmtree(distdir)

mkdir(distdir)

"""
Compile pyc file.
"""
pycpath_str = "__pycache__\\"
pycpath = pathlib.Path(pycpath_str)
if pycpath.exists():
    shutil.rmtree(pycpath)
compile_excludes = ["setup.py", "build_pyc.py"]
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
for f in pycpath.iterdir():
    m = prog.fullmatch(str(f).replace(abspath(str(pycpath)), ""))
    if m is not None:
        f.rename(m.group(1) + ".pyc")
for f in pycpath.iterdir():
        shutil.copy(f, distdir + str(f).replace(str(pycpath_str), ""))

def copydir(path: pathlib.Path):
    """
    Copy directory.
    """
    mkdir(distdir + str(path).replace(abspath("."), ""))
    for file in path.iterdir():
        if file.is_dir():
            copydir(file)
        else:
            shutil.copy(file, distdir + str(file).replace(abspath("."), ""))

"""
Copy resources files.
"""
for file in list(dict(dict(dict(dict(toml.loads(open("pyproject.toml", "r", encoding="utf-8").read())).get("tool")).get("distutils")).get("build_exe")).get("include_files")):
    file = str(file)
    filep = pathlib.Path(file)
    if filep.is_dir():
        copydir(pathlib.Path(file))
    else:
        shutil.copy(file, distdir + file.replace(abspath("."), ""))
