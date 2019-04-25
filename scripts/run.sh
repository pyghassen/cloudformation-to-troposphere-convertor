#!/bin/sh
set -e

# FILE_INPUT=cloudformation_template_examples/template_development.json
# FILE_OUTPUT=troposhphere_generated_files/toposhphere_template_development.json
#
echo "Converting $1 .."
python run.py $1 $2
echo "You can find output in $2 .."
