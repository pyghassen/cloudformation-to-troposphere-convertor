from troposphere import Template, Ref, Output

from app.factories import create_template


def test_create_template():
    description = "Test description"
    metadata = {
        "Metadata": {
            "DependsOn": [],
            "Environment": "Development",
            "StackName": "Development-VPC"
        }
    }
    internet_gateway_output = Output("InternetGateway", Value=Ref("InternetGateway"))
    vpc_id_output = Output("VPCID", Value=Ref("VPC"))

    outputs = [internet_gateway_output, vpc_id_output]

    expected_output = {
        "InternetGateway": internet_gateway_output,
        "VPCID": vpc_id_output
    }

    resources = []

    expected_resources = {}

    template = create_template(description, metadata, outputs, resources)

    assert isinstance(template, Template)
    assert template.description == description
    assert template.metadata == metadata
    assert template.outputs == expected_output
    assert template.resources == expected_resources
