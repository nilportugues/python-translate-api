# Generate release tarball
cd src/
python setup.py sdist
cd ..

# save somewhere the build at: 
mv ./src/dist/translate_api-0.1.tar.gz ./docker

