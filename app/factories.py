"""
Factories module contains all the factories functions to create troposphere
template.
"""
from troposphere import Template


def create_template(description, metadata, outputs):
    """Creates troposphere template."""
    template = Template()
    template.set_description(description)
    template.set_metadata(metadata)
    template.add_output(outputs)

    return template
