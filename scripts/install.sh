#!/bin/bash
# installation steps
cd `dirname $0`
cd ../
python -V
echo "`which pip`, continue?"
read
easy_install -U setuptools
pip install -r requirements/debug.txt
