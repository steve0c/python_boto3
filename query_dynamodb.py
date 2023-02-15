
from boto3.dynamodb.conditions import Key #importing key and attr ***You will recieve error if not imported


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('DynamoDB_Python') #var for table name

response = table.query( 
  KeyConditionExpression=Key('country').eq('Thailand')   #query for items with "Country" "Thailand"
)

