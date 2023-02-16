import boto3

vpc = boto3.client("ec2")

response = vpc.describe_vpcs()

print(response)
