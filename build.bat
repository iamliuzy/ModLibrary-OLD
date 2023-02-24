cd __pycache__
del *.pyc
cd ..
python -m compileall . -l -o 2
cd __pycache__
set "str=.cpython-310.opt-2"
setlocal EnableDelayedExpansion
for /f "delims=" %%i in ('dir /b *.cpython-310.opt-2.pyc') do (
set "var=%%i" & ren "%%i" "!var:%str%=!")
cd ..
xcopy __pycache__ dist\ /E /Y
