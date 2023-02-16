# creating an ec2 instance 

import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="************", #insert AMI
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="KeyPair1"
    )