import boto3
import json
from datetime import datetime
import time

dynamodb = boto3.client('dynamodb')
tableName = 'ddbgsi2-DynamoDBTable-198MO0TAA4NVI'

teams = {'rugby', 'soccer', 'hockey', 'hurling', 'football'}
for team in teams:
    print(str(datetime.now()))
    for i in range(100,1000):
        item = {
        "pk1": {
            "S": str(i) 
        },
        "sk1": {
            "S": team
        },
        "team": {
            "S": team
        },
        "player": {
            "S": "Jack"
        }
        }
        response = dynamodb.put_item(
            TableName=tableName,
            Item=item
            )
        #sprint(item)
        #time.sleep(1)