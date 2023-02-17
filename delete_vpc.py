# delete a vpc

import boto3

vpc = boto3.client("ec2")

response = vpc.delete_vpc(
    VpcId='vpc-0362d507dda6e633f'  #vpc id is required
    )
    
print(response)
    
    