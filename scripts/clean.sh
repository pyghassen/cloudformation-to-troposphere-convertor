#!/bin/sh

echo "Removing the python and pytest cache files"
set -e
find . -type d -name __pycache__ | xargs rm -rf
rm -rf .pytest_cache/
