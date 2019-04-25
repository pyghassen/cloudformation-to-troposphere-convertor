"""
Convertor module contains the convert_to_troposphere function which create a
troposphere file out of cloudformation template.
"""

from app.factories import create_template, create_resource
from app.helpers import (
    get_description, get_metadata, get_outputs, get_resources
)


def convert_to_troposphere(data):
    """Converts a cloudformation template file content to troposphere."""
    description = get_description(data)
    metadata = get_metadata(data)

    outputs = get_outputs(data)

    resources = [
        create_resource(resource_title, resource_values)
        for resource_title, resource_values in get_resources(data).items()
    ]

    template = create_template(description, metadata, outputs, resources)

    return template.to_json()
