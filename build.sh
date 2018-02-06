#!/bin/bash
CWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Generate release tarball
cd $CWD/src/
python3 setup.py sdist
cd ..

# save somewhere the build at: 
mv $CWD/src/dist/translate_api-0.1.tar.gz $CWD/docker

