import pytest

from troposphere import Output, Ref, ec2

from app.helpers import (
    get_description, get_metadata, get_outputs, get_resources,
    get_resource_type_name, get_property, get_properties
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
        },
        "VpcGatewayAttachment": {
            "Properties": {
                "InternetGatewayId": {
                    "Ref": "InternetGateway"
                },
                "VpcId": {
                    "Ref": "VPC"
                }
            },
            "Type": "AWS::EC2::VPCGatewayAttachment"
        },
        "VpcNetworkAcl": {
            "Properties": {
                "Tags": [
                    {
                        "Key": "Environment",
                        "Value": "Development"
                    },
                    {
                        "Key": "Name",
                        "Value": "Development-NetworkAcl"
                    }
                ],
                "VpcId": {
                    "Ref": "VPC"
                }
            },
            "Type": "AWS::EC2::NetworkAcl"
        },
        "VpcNetworkAclInboundRule": {
            "Properties": {
                "CidrBlock": "0.0.0.0/0",
                "Egress": "false",
                "NetworkAclId": {
                    "Ref": "VpcNetworkAcl"
                },
                "PortRange": {
                    "From": "443",
                    "To": "443"
                },
                "Protocol": "6",
                "RuleAction": "allow",
                "RuleNumber": 100
            },
            "Type": "AWS::EC2::NetworkAclEntry"
        },
        "VpcNetworkAclOutboundRule": {
            "Properties": {
                "CidrBlock": "0.0.0.0/0",
                "Egress": "true",
                "NetworkAclId": {
                    "Ref": "VpcNetworkAcl"
                },
                "Protocol": "6",
                "RuleAction": "allow",
                "RuleNumber": 200
            },
            "Type": "AWS::EC2::NetworkAclEntry"
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
        ({"Type": "AWS::EC2::NetworkAclEntry"}, "NetworkAclEntry"),
        # ({"Type": "AWS::EC2::NetworkAcl"}, "NetworkAcl"),
    ]
)
def test_get_resource_type_name(resource_values, expected_type_name):
    resource_type_name = get_resource_type_name(resource_values)
    assert resource_type_name == expected_type_name


def test_get_property_takes_integer_value():
    assert get_property('RuleNumber', 100) == {'RuleNumber': '100'}


def test_get_property_takes_string_value():
    expected_data = {'CidrBlock': '10.0.0.0/16'}
    assert get_property('CidrBlock', '10.0.0.0/16') == expected_data


def test_get_property_takes_dictionary_value():
    expected_data = {
        'Tags': [
            {'Key': 'Environment', 'Value': 'Development'},
            {'Key': 'Name', 'Value': 'Development-InternetGateway'}
        ]
    }

    property_values = [
        {'Key': 'Environment', 'Value': 'Development'},
        {'Key': 'Name', 'Value': 'Development-InternetGateway'}
    ]

    assert get_property('Tags', property_values) == expected_data


def test_get_property_takes_ec2_ref():
    ec2_ref = Ref("InternetGateway")
    expected_data = {"InternetGatewayId": ec2_ref}

    property_values = {'Ref': 'InternetGateway'}

    assert get_property("InternetGatewayId", property_values) == expected_data


def test_get_property_takes_ec2_port_range():
    property_values = {'From': '443', 'To': '443'}

    _property = get_property('PortRange', property_values)
    property_name, property_value = _property.popitem()

    assert property_name == 'PortRange'
    assert isinstance(property_value, ec2.PortRange)


@pytest.mark.parametrize(
    "resource_values,expected_properties",
    [
        (
            {
                'Properties':
                    {
                        'Tags': [
                            {'Key': 'Environment', 'Value': 'Development'},
                            {'Key': 'Name', 'Value': 'Development-InternetGateway'} # noqa
                        ]
                    },
                'Type': 'AWS::EC2::InternetGateway'
            },
            {
                'Tags': [
                    {'Key': 'Environment', 'Value': 'Development'},
                    {'Key': 'Name', 'Value': 'Development-InternetGateway'}
                ]
            }
        ),
        (
            {
                'Properties': {
                    'CidrBlock': '10.0.0.0/16',
                    'EnableDnsHostnames': 'true',
                    'EnableDnsSupport': 'true',
                    'InstanceTenancy': 'default',
                    'Tags': [
                        {'Key': 'Environment', 'Value': 'Development'},
                        {'Key': 'Name', 'Value': 'Development-ServiceVPC'}
                    ]
                },
                'Type': 'AWS::EC2::VPC'
            },
            {
                'CidrBlock': '10.0.0.0/16',
                'EnableDnsHostnames': 'true',
                'EnableDnsSupport': 'true',
                'InstanceTenancy': 'default',
                'Tags': [
                    {'Key': 'Environment', 'Value': 'Development'},
                    {'Key': 'Name', 'Value': 'Development-ServiceVPC'}
                ]
            }
        ),
    ]
)
def test_get_properties(resource_values, expected_properties):
    properties = get_properties(resource_values)
    assert properties == expected_properties
