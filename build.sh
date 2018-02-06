#!/bin/bash

# Generate release tarball
cd ./src/
python3 setup.py sdist
cd ..

# save somewhere the build at: 
mv ./src/dist/translate_api-0.1.tar.gz ./docker

