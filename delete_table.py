import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('DynamoDB_Python') #var for table name

response = table.delete()

print(responce)