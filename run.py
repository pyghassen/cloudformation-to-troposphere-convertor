import json

import click

from app.convertor import convert_to_troposphere


@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def convert(input, output):
    """
    This script takes a cloudformation template file and converts it to
    troposphere.
    """

    data = json.loads(input.read())
    result = convert_to_troposphere(data)

    output.write(result)
    output.flush()


if __name__ == '__main__':
    convert()
