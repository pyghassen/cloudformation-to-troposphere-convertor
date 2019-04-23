"""
Helpers module conatains helper function to extract data from the input file.
"""
from troposphere import Ref, Output


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
