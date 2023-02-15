


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('DynamoDB_Python') #var for table name

#delete item 
response = table.delete_item(
    Key={
        'country': 'Thailand', 'city': 'Pai'})
        
print(response) #print response 
