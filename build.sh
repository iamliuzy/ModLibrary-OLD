python -m compileall . -l -f -i build.txt -o 2
cd __pycache__ || exit
rename cpython-*.pyc .pyc *.pyc
cp -r pack_resources/ __pycache__
