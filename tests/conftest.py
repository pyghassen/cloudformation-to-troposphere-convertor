import pytest


@pytest.fixture
def data():
    return {
        "Description": "Service VPC",
        "Metadata": {
            "DependsOn": [],
            "Environment": "Development",
            "StackName": "Development-VPC"
        },
        "Outputs": {
            "InternetGateway": {
                "Value": {
                    "Ref": "InternetGateway"
                }
            },
            "VPCID": {
                "Value": {
                    "Ref": "VPC"
                }
            }
        },
        "Resources": {
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
    }
