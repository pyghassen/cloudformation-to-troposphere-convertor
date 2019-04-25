"""
Helpers module conatains helper function to extract description, metadata,
outputs, resources from the cloudformation template file content.
"""
from troposphere import Ref, Output, ec2


def get_description(data):
    """Gets description from the input cloutformation file content."""
    return data['Description']


def get_metadata(data):
    """Gets metadata from the input cloutformation file content."""
    return data['Metadata']


def get_outputs(data):
    """Gets outputs from the input cloutformation file content."""
    outputs = data['Outputs']
    return [
        Output(output_name, Value=Ref(output_values['Value']['Ref']))
        for output_name, output_values in outputs.items()
    ]


def get_resources(data):
    """Gets resources from the input cloutformation file content."""
    return data['Resources']


def get_resource_type_name(resource_values):
    """Gets resource type name from resource values."""
    resource_type = resource_values['Type']
    return resource_type.split('::')[-1]


def get_property(property_name, property_values):
    if type(property_values) is int:
        data = {property_name: str(property_values)}
    elif 'Ref' in property_values:
        data = {property_name: Ref(property_values['Ref'])}
    elif 'PortRange' in property_name:
        data = {property_name: ec2.PortRange(**property_values)}
    else:
        data = {property_name: property_values}

    return data


def get_properties(resource_values):
    properties = {}
    properties_data = resource_values['Properties']

    for property_name, property_values in properties_data.items():
        property = get_property(property_name, property_values)
        properties.update(property)

    return properties
