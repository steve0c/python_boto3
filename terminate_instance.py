import boto3

ec2 = boto3.client('ec2')

response = ec2.terminate_instances(InstanceIds=['***********']) #insert instance ID

print(response)