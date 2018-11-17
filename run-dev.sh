#!/usr/bin/env bash
pip2 install virtualenv

pyvenv venv
source venv/bin/activate
pip2 install -r src/translate_api/requirements.txt
export PYTHONPATH=.:$PYTHONPATH
python2 src/translate_api/application_dev.py
