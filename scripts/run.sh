#!/bin/sh
set -e

FILE_INPUT=cloudformation_template_examples/template_development.json
FILE_OUTPUT=troposhphere_generated_files/toposhphere_template_development.json

echo "Converting $FILE_INPUT .."
python run.py $FILE_INPUT $FILE_OUTPUT
echo "You can find output in $FILE_OUTPUT .."
