"""
Factories module contains all the factories functions to create troposphere
template and resources.
"""
from troposphere import Template, ec2
from app.helpers import get_resource_type_name, get_properties


def create_template(description, metadata, outputs, resources):
    """Creates troposphere template."""
    template = Template()
    template.set_description(description)
    template.set_metadata(metadata)
    template.add_output(outputs)
    for resource in resources:
        template.add_resource(resource)
    return template


def create_resource(resource_title, resource_values):
    """Creates troposphere resource."""
    resource_type_name = get_resource_type_name(resource_values)
    resource_class = getattr(ec2, resource_type_name)
    properties = get_properties(resource_values)
    return resource_class(resource_title, **properties)
