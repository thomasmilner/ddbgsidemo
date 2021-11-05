import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime

region="eu-west-1"
# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name=region)
dynamodb = boto3.resource('dynamodb', region_name=region)

# Creating the DynamoDB Table Resource
#dynamodb = boto3.resource('dynamodb', region_name="eu-west-1")
#table = dynamodb.Table(TABLE_NAME)

#scenario1
TABLE_NAME = "ddbgsi1-DynamoDBTable-3H9WUWBV2BXG"
table = dynamodb.Table(TABLE_NAME)
print('scenario1_query1')
print(str(datetime.now()))
for i in range(1,100):
    response = table.scan(FilterExpression=Key('sk1').eq('0') )

    result = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(FilterExpression=Key('sk1').eq('0') )
        result.extend(response['Items'])

print(str(datetime.now()))

print('scenario1_query2')
print(str(datetime.now()))
for i in range(1,100):
    response = dynamodb_client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression='pk1 = :team',
        ExpressionAttributeValues={
            ':team': {'S': 'rugby'}
        }
    )
print(str(datetime.now()))
#data = response['Items']

#fe = Key('sk#1').eq('0')

#response = dynamodb_client.scan(
#    TableName=TABLE_NAME,
#    FilterExpression=fe
#)

#scenario2
TABLE_NAME = "ddbgsi2-DynamoDBTable-198MO0TAA4NVI"
table = dynamodb.Table(TABLE_NAME)

print('scenario2_query1')
print(str(datetime.now()))
for i in range(1,100):
    response = dynamodb_client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression='pk1 = :index',
        ExpressionAttributeValues={
            ':index': {'S': '0'}
        }
    )
print(str(datetime.now()))

print('scenario2_query2')
print(str(datetime.now()))
for i in range(1,100):
    response = table.scan(FilterExpression=Key('sk1').eq('rugby') )

    result = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(FilterExpression=Key('sk1').eq('rugby') )
        result.extend(response['Items'])

print(str(datetime.now()))

#scenario3
TABLE_NAME = "ddbgsi3-DynamoDBTable-3JF414EM6UC3"

print('scenario3_query1')
print(str(datetime.now()))
for i in range(1,100):
    response = dynamodb_client.query(
        TableName=TABLE_NAME,
        IndexName="gsi1",
        KeyConditionExpression='sk1 = :index',
        ExpressionAttributeValues={
            ':index': {'S': '0'}
        }
    )
print(str(datetime.now()))

print('scenario3_query2')
print(str(datetime.now()))
for i in range(1,100):
    response = dynamodb_client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression='pk1 = :team',
        ExpressionAttributeValues={
            ':team': {'S': 'rugby'}
        }
    )
print(str(datetime.now()))

#scenario4
TABLE_NAME = "ddbgsi4-DynamoDBTable-O1ZZDKST5R1N"

print('scenario4_query1')
print(str(datetime.now()))
for i in range(1,100):
    response = dynamodb_client.query(
        TableName=TABLE_NAME,
        IndexName="gsi1",
        KeyConditionExpression='gsi_pk1 = :index',
        ExpressionAttributeValues={
            ':index': {'S': '0'}
        }
    )

print(str(datetime.now()))

print('scenario4_query2')
print(str(datetime.now()))
for i in range(1,100):
    response = dynamodb_client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression='pk1 = :team',
        ExpressionAttributeValues={
            ':team': {'S': 'rugby'}
        }
    )
print(str(datetime.now()))
