python -m compileall . -l -f -i build.txt -o 2
cd __pycache__
set "str=.cpython-310.opt-2"
setlocal EnableDelayedExpansion
for /f "delims=" %%i in ('dir /b *.cpython-311.opt-2.pyc') do (
set "var=%%i"
ren "%%i" "!var:%str%=!")
cd ..
xcopy pack_resources __pycache__ /E /Y
