import pytest
from troposphere import Output

from app.helpers import get_description, get_metadata, get_outputs


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
    }

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
