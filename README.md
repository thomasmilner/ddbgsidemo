# DyanamoDB Single Table Design GSI test

4 AWS SAM applications that show how a GSI can help improve access patterns on a DynamoDB table

## Requirements
Install AWS SAM CLI by following [their installation instructions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).

## Files
There are 4 separate applications in the repo

../Table1
../Table2
../Table3
../Table4

Each application can be deployed as it's own SAM application but the folder structure is the same for each

../Table1/template.yml - SAM template to create DynamoDB table, stream and Lambda to process stream. Lambda is written in Python 3.8 runtime
../Table1/streamsdemo/app.py - Lambda code
../Table1/tests/dataload.py - generate data and insert into table

Tests are stored in a folder at the same level
../tests/dbreadop1.py - execute tests for access pattern 1 against all 4 tables
../tests/dbreadop2.py - execute tests for access pattern 2 against all 4 tables
../tests/dbreadoperations.py - execute tests for both access patterns against all 4 tables

## Blog
Read this [article](https://dev.to/tom_millner/dynamodb-when-to-use-a-gsi-6h5-temp-slug-8425817) to walk through tutorial and details/learnings on how I built this application

