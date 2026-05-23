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

#creating a public subnet
public_subnet = aws.ec2.Subnet("public-subnet", {
    vpc_id = vpc.id,
    cidr_block = "10.0.1.0/24",
    availability_zone="ap-southeast-1a",
    map_public_ip_on_launch=True,
    tags={
        "Name": "public-subnet"
    }
})

pulumi.export("public_subnet_id", public_subnet.id)