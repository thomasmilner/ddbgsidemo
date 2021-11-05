import json
import boto3
import traceback
from botocore.exceptions import ClientError

def updateDDBTable(tableName,pkValue,team,counter):
    dynamodb = boto3.resource('dynamodb')
     
    #Get table name from stream. Updates will be written back to same table
    dynamodb_table = dynamodb.Table(tableName)
    
    #loop through collection
    dynamodb_table.update_item(
            Key={
                    'pk1': pkValue,
                    'sk1': '0'             
                },
            UpdateExpression="set cnt = ((if_not_exists(cnt,:init)) + :num), gsi_pk1 = :zero, gsi_sk1 = :team, team = :team  ", #if record doesn't exist, create it
            ExpressionAttributeValues={
                    ':init': 0, #new record will be created with 0 + num value
                    ':num': counter,
                    ':zero': '0',
                    ':team': team
                },
            ReturnValues="NONE"
            )
                
def updateCounter(tableName,pkValue,team,counter):
    #persist changes to table
    updateDDBTable(tableName,pkValue,team,counter)
    
def parseStreamArn(streamARN):
    tableName = streamARN.split(':')[5].split('/')[1]
    return(tableName)

def _lambda_handler(event, context):

    records = event['Records']

    record1 = records[0]
    tableName = parseStreamArn(record1['eventSourceARN'])
 
    for record in records:

        event_name = record['eventName'].upper()  # INSERT, MODIFY, REMOVE
        pkValue = record['dynamodb']['Keys']['pk1']['S']
        team = record['dynamodb']['NewImage']['team']['S']
        #print(keyValue)
        
        if (event_name == 'INSERT') and "cnt" not in record['dynamodb']["NewImage"]:
            print(event_name)
            updateCounter(tableName,pkValue,team,1)

        #if (event_name == 'REMOVE') and "sales_cnt" not in record['dynamodb']["NewImage"]:
        #    updateCounter(tableName,pkValue,skValue,-1)
            
    return 'Successfully processed {} records.'.format(len(event['Records']))
    
def lambda_handler(event, context):
    try:
        return _lambda_handler(event, context)
    except Exception:
        print (traceback.format_exc())
