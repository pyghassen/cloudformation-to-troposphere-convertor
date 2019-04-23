#!/bin/sh
set -e

echo "Running pylint .."
pylint app

if [ "$ENV" = "CI" ]
then
  echo "Running codecov .."
  codecov
fi
