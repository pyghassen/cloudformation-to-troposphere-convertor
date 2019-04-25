import pytest

from troposphere import Output

from app.helpers import (
    get_description, get_metadata, get_outputs, get_resources,
    get_resource_type_name
)


def test_get_description(data):
    description = get_description(data)
    assert description == "Service VPC"


def test_get_metadata(data):
    expected_data = {
        "DependsOn": [],
        "Environment": "Development",
        "StackName": "Development-VPC"
    }

    metadata = get_metadata(data)
    assert metadata == expected_data


def test_get_outputs(data):
    expected_output_titles = ["InternetGateway", "VPCID"]
    outputs = get_outputs(data)
    assert len(outputs) == 2
    for output in outputs:
        assert isinstance(output, Output)
        assert output.title in expected_output_titles


def test_get_resources(data):
    expected_data = {
        "InternetGateway": {
            "Properties": {
                "Tags": [
                    {
                        "Key": "Environment",
                        "Value": "Development"
                    },
                    {
                        "Key": "Name",
                        "Value": "Development-InternetGateway"
                    }
                ]
            },
            "Type": "AWS::EC2::InternetGateway"
            },
            "VPC": {
                "Properties": {
                    "CidrBlock": "10.0.0.0/16",
                    "EnableDnsHostnames": "true",
                    "EnableDnsSupport": "true",
                    "InstanceTenancy": "default",
                    "Tags": [
                        {
                            "Key": "Environment",
                            "Value": "Development"
                        },
                        {
                            "Key": "Name",
                            "Value": "Development-ServiceVPC"
                        }
                    ]
                },
                "Type": "AWS::EC2::VPC"
            }
        }

    resources = get_resources(data)
    assert resources == expected_data


@pytest.mark.parametrize(
    "resource_values,expected_type_name",
    [
        ({"Type": "AWS::EC2::InternetGateway"}, "InternetGateway"),
        ({"Type": "AWS::EC2::VPC"}, "VPC"),
        ({"Type": "AWS::EC2::VPCGatewayAttachment"}, "VPCGatewayAttachment"),
        ({"Type": "AWS::EC2::NetworkAcl"}, "NetworkAcl"),
    ]
)
def test_get_resource_type_name(resource_values, expected_type_name):
    resource_type_name = get_resource_type_name(resource_values)
    assert resource_type_name == expected_type_name
