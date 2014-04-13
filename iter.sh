#!/bin/bash

echo -e 'y\n' | pip uninstall simple_threadpool
rm -f dist/*
python setup.py sdist
pip install dist/*.gz

# upload
# python setup.py sdist bdist_wininst upload
