#!/bin/bash

echo 'Setting up project dependencies'

sudo apt-get install libffi-dev

echo 'Getting TA-lib source:'

sudo wget -P /tmp http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz 

sudo tar -xv -C /tmp -f /tmp/ta-lib-0.4.0-src.tar.gz

cd /tmp/ta-lib

echo 'Configure installation dir:'

./configure --prefix=/usr

echo 'Building and Installing TA-lib:'

make || sudo make install 

echo 'Installing python-dependencies from requirements file:'

cd -

python3 -m pip install -r requirements.txt

echo 'Clean Up'

sudo rm -r /tmp/ta-lib-0.4.0-src.tar.gz /tmp/ta-lib