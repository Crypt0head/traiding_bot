echo off
echo Setting up project dependencies

echo Your python version is:

python -V

python -m pip install --upgrade pip

echo Installing TA-lib .whl file:

python -m pip install .\test_bot\libs\TA_Lib-0.4.21-cp38-cp38-win_amd64.whl

echo Installing python-dependencies from requirements file:

python -m pip install -r .\test_bot\requirements.txt