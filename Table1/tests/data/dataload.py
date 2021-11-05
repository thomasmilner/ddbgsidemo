import boto3
import json
from datetime import datetime
import time

dynamodb = boto3.client('dynamodb')
tableName = 'ddbgsi1-DynamoDBTable-3H9WUWBV2BXG'

teams = {'rugby', 'soccer', 'hockey', 'hurling', 'football'}
for team in teams:
    print(str(datetime.now()))
    for i in range(100,1000):
        item = {
        "pk1": {
            "S": team
        },
        "sk1": {
            "S": str(i) 
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
        #print(item)
        #time.sleep(1)