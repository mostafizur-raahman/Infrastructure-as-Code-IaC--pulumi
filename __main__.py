"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import AWS


#vpc creating
vpc = aws.ec2.Vpc("my-vpc", {
    cidr_block = "10.0.0.0/16",
    tags = {
        "Name": "my-vpc"
    }
})

pulumi.export("vpc_id", vpc_id)