#import boto3
import json
from datetime import datetime
#import time

#dynamodb = boto3.client('dynamodb')
#tableName = 'streamsdemo'

teams = {'rugby', 'soccer', 'hockey', 'hurling', 'football'}
for team in teams:
    #orderdatetime = str(datetime.now())
    for i in range(1,100):
        #productKey = 'PROD#000' + str(j)
        item = {
        "pk1": {
            "S": team
        },
        "sk1": {
            "S": i 
        },
        "team": {
            "S": team
        },
        "player": {
            "S": "Jack"
        },
        "gsi_pk1": {
            "S": 1
        },
        "gsi_sk1": {
            "S": team
        }
        }
        #response = dynamodb.put_item(
        #    TableName=tableName,
        #    Item=item
        #    )
        print(item)
        #time.sleep(1)