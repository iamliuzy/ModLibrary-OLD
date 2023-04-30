python -m compileall -l -f -i build.txt -o 2 -b
xcopy .\*.pyc .\__pycache__\ /Y /K
del .\*.pyc
xcopy pack_resources __pycache__ /E /Y
