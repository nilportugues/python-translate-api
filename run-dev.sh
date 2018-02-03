#!/usr/bin/env bash

pip install virtualenv


pyvenv venv
source venv/bin/activate
pip install -r src/translate_api/requirements.txt
export PYTHONPATH=.:$PYTHONPATH
python src/translate_api/application_dev.py